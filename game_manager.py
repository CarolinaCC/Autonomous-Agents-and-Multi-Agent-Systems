from agent.rl import ReinforcementLearning
from central_bank import CentralBank
from agent.agent import *
from agent.gold_standard import *
from agent.simple_reactive import *
import os
import sys
import random as rd

import json

from event.event import Event, NoneEvent
from stock import Stock, StockRelation


class GameManager:
    event = False


    def __init__(self,
                 random_agents_num, simple_react_agents_num,
                 careful_react_agents_num, steps_num,
                 mode="DEFAULT"):
        self.random_agents_num = random_agents_num
        self.simple_react_agents_num = simple_react_agents_num
        self.careful_react_agents_num = careful_react_agents_num
        self.steps_num = steps_num
        self.game_mode = mode
        self.central_bank, self.events = self.setup_world()
        self.agents_array = []
        self.setup_agents()
        self.current_step = 0
        self.end_flag = False
        self.current_event = NoneEvent(1)

    def setup_world(self):

        min_price = 0.0001
        enron = Stock("Enron", 0, 2.6, 1.03, 0.005, min_price, self.game_mode)
        galp = Stock("Galp", 1, 2.9, 1.03, 0.004, min_price, self.game_mode)
        primark = Stock("Primark", 2, 2.2, 1.025, 0.006, min_price, self.game_mode)
        tesla = Stock("Tesla", 3, 3.1, 1.05, 0.001, min_price, self.game_mode)
        moderna = Stock("Moderna", 4, 3.3, 1.01, 0.002, min_price, self.game_mode)
        microsoft = Stock("Microsoft", 5, 2.2, 1.02, 0.003, min_price, self.game_mode)
        aldi = Stock("Aldi", 6, 4.1, 1.025, 0.006, min_price, self.game_mode)
        intel = Stock("Intel", 7, 3.1, 1.05, 0.001, min_price, self.game_mode)
        stocks = [enron, galp, primark, tesla, moderna, microsoft, aldi, intel]

        stock_relations = [StockRelation(enron, galp, -0.00003),
                           StockRelation(primark, aldi, -0.00002),
                           StockRelation(tesla, intel, 0.00005),
                           StockRelation(microsoft, intel, 0.00003)
                           ]
        event_list = []
        bank = CentralBank(stocks, stock_relations)
        
        if self.game_mode == "DEFAULT":
            print("ENTREI NESTE IF") #Não está a entrar aqui
            covid_event = Event("Covid-19", [[1.1],[1.3],[1.4],[1.4]], 4, [moderna])
            tech_boom_event = Event("Tech Boom", [[1.2,1.2,1.2],[1.2,1.2,1.2],[1.1,1.1,1.1],[1.05,1.05,1.05]], 4, [microsoft, tesla, intel])
            oil_crisis_event = Event("Oil Crisis", [[0.85,0.85],[0.85,0.85],[0.95,0.95]], 3, [enron, galp])
            tech_breakthrough_event = Event("Tech Breakthrough", [[1.3,0.9,0.9],[1.2,1,1]], 2, rd.sample([microsoft, tesla, intel],3))
            positive_elon_tweet = Event("Positive Crazy Elon Musk Tweet",[[1.5,0,0,0,0,0,0,0],[0.8,0,0,0,0,0,0,0],[0.9,0,0,0,0,0,0,0]],3,rd.sample([enron, galp, primark, tesla, moderna, microsoft, aldi, intel],8))
            negative_elon_tweet = Event("Negative Crazy Elon Musk Tweet",[[0.7,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1.1,0,0,0,0,0,0,0]],3,rd.sample([enron, galp, primark, tesla, moderna, microsoft, aldi, intel],8))
            event_list = [covid_event, tech_breakthrough_event, tech_boom_event, oil_crisis_event,positive_elon_tweet,negative_elon_tweet]
        return(bank,event_list)

    def get_random_agents(self):
        return self.random_agents_num

    def setup_agents(self):
        for _ in range(self.random_agents_num):
            self.agents_array.append(RandomAgent(self.central_bank))
        for _ in range(self.simple_react_agents_num):
            self.agents_array.append(SimpleReactive(self.central_bank))
        for _ in range(self.careful_react_agents_num):
            self.agents_array.append(Careful(self.central_bank))
        # TODO add new agents

    def step(self, num_steps):
        if self.has_ended():
            return
        for _ in range(num_steps):
            if self.current_step >= self.steps_num:
                self.end_flag = True
                return
            if self.game_mode == "DEFAULT":
                self.update_event()
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()
            #self.events.next().update()
            self.current_step += 1
            for agent in self.agents_array:
                if isinstance(agent, ReinforcementLearning):
                    agent.learn()

    def enable_event(self):
        self.event = True

    def update_event(self):
        if not self.current_event.is_over:
            self.current_event.update()
        else:
            self.current_event = self.current_event.reset()
            self.current_event = self.choose_next_event()
            self.current_event.update()
        return
    
    def choose_next_event(self):
        if rd.random() < 0.75:
            return(NoneEvent(1))
        else:
            return(rd.choice(self.events))
        

    def get_current_event(self):
        return self.current_event.name

    def has_ended(self):
        return self.end_flag

    def print_results(self):
        i = 0
        # FIXME
        while os.path.exists("outputs/stock_history" + str(i) + ".json"):
            i += 1
        with open("outputs/stock_history" + str(i) + ".txt", 'w', encoding='utf-8') as f:
            for stock in self.central_bank.stocks:
                f.write(repr(stock))
            #     json.dump(stock.toJSON(), f, ensure_ascii=False, indent=4)

        # with open("agent_history" + str(i) + ".txt", 'w', encoding='utf-8') as f:
        #     for a in self.agents_array:
        #         json.dump(a, f, ensure_ascii=False, indent=4)
