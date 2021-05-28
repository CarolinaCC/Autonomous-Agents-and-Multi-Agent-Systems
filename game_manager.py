import random

from agent.careful import Careful
from agent.rl import ReinforcementLearning
from central_bank import CentralBank
from agent.agent import *
from agent.simple_reactive import *
import os
import random as rd

from event import Event, NoneEvent, EventIterator
from stock import Stock, StockRelation


class GameManager:
    event = False

    def __init__(self,
                 random_agents_num, simple_react_agents_num,
                 careful_react_agents_num, rl_agents_num,
                 steps_num,
                 mode="DEFAULT"):
        self.random_agents_num = random_agents_num
        self.simple_react_agents_num = simple_react_agents_num
        self.careful_react_agents_num = careful_react_agents_num
        self.rl_agents_num = rl_agents_num
        self.steps_num = steps_num
        self.game_mode = mode
        self.central_bank, self.events = self.setup_world()
        self.events = EventIterator(self.events)
        self.agents_array = []
        self.setup_agents()
        self.current_step = 0
        self.end_flag = False
        self.current_event = NoneEvent(1)

    def setup_world(self):

        min_price = 0.0001
        bp = Stock("BP", 0, 2.6, 0.9997, 0.00005, min_price, self.game_mode, 95452)
        galp = Stock("Galp", 1, 2.9, 1.0003, 0.00004, min_price, self.game_mode, 48324)
        primark = Stock("Primark", 2, 0.98, 1.00025, 0.00006, min_price, self.game_mode, 14437)
        tesla = Stock("Tesla", 3, 3.1, 1.0005, 0.00001, min_price, self.game_mode, 12358)
        moderna = Stock("Moderna", 4, 3.3, 1.0001, 0.00002, min_price, self.game_mode, 84562)
        microsoft = Stock("Microsoft", 5, 2.2, 1.000015, 0.00003, min_price, self.game_mode, 12357)
        aldi = Stock("Aldi", 6, 4.1, 1.00025, 0.00006, min_price, self.game_mode, 84651)
        intel = Stock("Intel", 7, 3.1, 1.0004, 0.00001, min_price, self.game_mode, 51278)
        self.stocks = [bp, galp, primark, tesla, moderna, microsoft, aldi, intel]

        stock_relations = [StockRelation(bp, galp, -0.000000003),
                           StockRelation(primark, aldi, -0.000000002),
                           StockRelation(tesla, intel, 0.0000000005),
                           StockRelation(microsoft, intel, 0.0000000003)
                           ]
        event_list = []
        bank = CentralBank(self.stocks, stock_relations, self.game_mode)

        if self.game_mode == "DEFAULT":
            covid_event = Event("Covid-19", 1.03, self.steps_num // 10, [moderna])
            covid_2nd_wave_event = Event("Covid-19 2nd wave", 1.03, self.steps_num // 10, [moderna])

            tech_boom_event = Event("Tech Boom", 1.04, self.steps_num // 10, [microsoft, tesla, intel])

            oil_crisis_event = Event("Oil Crisis", 0.993, self.steps_num // 8, [bp, galp])
            tech_breakdown_event = Event("Tech Boom", 0.994, self.steps_num // 12, [microsoft, tesla, intel])
            tmp = [covid_event, covid_2nd_wave_event, tech_breakdown_event, tech_boom_event]
            event_list = [NoneEvent(self.steps_num // 15), random.choice(tmp), random.choice(tmp),
                          NoneEvent(self.steps_num // 50), random.choice(tmp),
                          NoneEvent(self.steps_num // 10), random.choice(tmp), random.choice(tmp)]
        return bank, event_list

    def get_random_agents(self):
        return self.random_agents_num

    def setup_agents(self):
        if self.random_agents_num + self.simple_react_agents_num + self.careful_react_agents_num + self.rl_agents_num > 8:
            return
        for _ in range(self.random_agents_num):
            self.agents_array.append(RandomAgent(self.central_bank))
        for _ in range(self.simple_react_agents_num):
            self.agents_array.append(SimpleReactive(self.central_bank))
        for _ in range(self.careful_react_agents_num):
            self.agents_array.append(Careful(self.central_bank))

        for _ in range(self.rl_agents_num):
            self.agents_array.append(ReinforcementLearning(self.central_bank))

    def step(self, num_steps):
        if self.has_ended():
            return
        for _ in range(num_steps):
            if self.current_step >= self.steps_num:
                self.end_flag = True
                return
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()
            self.current_step += 1
            for agent in self.agents_array:
                if isinstance(agent, ReinforcementLearning):
                    agent.learn()
            if self.game_mode == "DEFAULT":
                self.events.next().update()

    def get_current_event(self):
        return self.events.next().name

    def has_ended(self):
        return self.end_flag
