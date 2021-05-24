from agent.rl import ReinforcementLearning
from central_bank import CentralBank
from agent.agent import *
from agent.gold_standard import *
from agent.simple_reactive import *
import os
import sys
import random as rd

import json

from event.event import EventIterator, Event, NoneEvent
from stock import Stock, StockRelation


class GameManager:
    event = False

    def __init__(self, random_agents_num, simple_react_agents_num, careful_react_agents_num, steps_num):
        self.random_agents_num = random_agents_num
        self.simple_react_agents_num = simple_react_agents_num
        self.careful_react_agents_num = careful_react_agents_num
        self.steps_num = steps_num
        self.central_bank, self.events = self.setup_world()
        self.agents_array = []
        self.setup_agents()
        self.current_step = 0
        # todo game mode
        self.game_mode = 'DEFAULT'
        self.end_flag = False

    def setup_world(self):
        enron = Stock("Enron", 0, 2.6, 1.03, 0.005)
        galp = Stock("Galp", 1, 2.9, 1.03, 0.004)
        primark = Stock("Primark", 2, 2.2, 1.025, 0.006)
        tesla = Stock("Tesla", 3, 3.1, 1.05, 0.001)
        modena = Stock("Modena", 4, 3.3, 1.01, 0.002)
        microsoft = Stock("Microsoft", 5, 2.2, 1.02, 0.003)
        aldi = Stock("Aldi", 6, 4.1, 1.025, 0.006)
        intel = Stock("Intel", 7, 3.1, 1.05, 0.001)
        stocks = [enron, galp, primark, tesla, modena, microsoft, aldi, intel]

        stock_relations = [StockRelation(enron, galp, -0.00003),
                           StockRelation(primark, aldi, -0.00002),
                           StockRelation(tesla, intel, 0.00005),
                           StockRelation(microsoft, intel, 0.00003)
                           ]

        bank = CentralBank(stocks, stock_relations)
        covid_event = Event("Covid-19", [1.1], 4, [modena])
        tech_boom_event = Event("Tech Boom", [1.2, 1.2, 1.2], 4, [microsoft, tesla, intel])
        oil_crisis_event = Event("Oil Crisis", [0.85, 0.85], 3, [enron, galp])
        tech_breakthrough_event = Event("TechBreakthrough", [1.3, 0.9, 0.9], 2, rd.sample([microsoft, tesla, intel], 3))
        event_list = [NoneEvent(2), covid_event, NoneEvent(3), tech_breakthrough_event, tech_boom_event,
                      oil_crisis_event]
        return bank, EventIterator(event_list)

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
            self.decide_event()
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()
            self.events.next().update()
            self.current_step += 1
            for agent in self.agents_array:
                if isinstance(agent, ReinforcementLearning):
                    agent.learn()

    def enable_event(self):
        self.event = True

    def decide_event(self):
        # TODO
        return

    def get_current_event(self):
        # TODO
        return self.events.next().name

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
