from agent.rl import ReinforcementLearning
from central_bank import CentralBank
from agent.agent import *
from agent.simple_reactive import *
import os
import random as rd

from event import Event, NoneEvent
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
        self.agents_array = []
        self.setup_agents()
        self.current_step = 0
        self.end_flag = False
        self.current_event = NoneEvent(1)

    def setup_world(self):

        min_price = 0.0001
        bp = Stock("BP", 0, 2.6, 0.99, 0.0005, min_price, self.game_mode, 95452)
        galp = Stock("Galp", 1, 2.9, 1.03, 0.0004, min_price, self.game_mode, 48324)
        primark = Stock("Primark", 2, 0.98, 1.025, 0.0006, min_price, self.game_mode, 14437)
        tesla = Stock("Tesla", 3, 3.1, 1.05, 0.0001, min_price, self.game_mode, 12358)
        moderna = Stock("Moderna", 4, 3.3, 1.01, 0.0002, min_price, self.game_mode, 84562)
        microsoft = Stock("Microsoft", 5, 2.2, 1.02, 0.0003, min_price, self.game_mode, 12357)
        aldi = Stock("Aldi", 6, 4.1, 1.025, 0.0006, min_price, self.game_mode, 84651)
        intel = Stock("Intel", 7, 3.1, 1.05, 0.0001, min_price, self.game_mode, 351278)
        self.stocks = [bp, galp, primark, tesla, moderna, microsoft, aldi, intel]

        stock_relations = [StockRelation(bp, galp, -0.00000003),
                           StockRelation(primark, aldi, -0.00000002),
                           StockRelation(tesla, intel, 0.000000005),
                           StockRelation(microsoft, intel, 0.000000003)
                           ]
        event_list = []
        bank = CentralBank(self.stocks, stock_relations, self.game_mode)
        
        if self.game_mode == "DEFAULT":
            covid_event = Event("Covid-19", [[1.1], [1.3], [1.4], [1.4]], 4, [moderna])
            tech_boom_event = Event("Tech Boom",
                                    [[1.2, 1.2, 1.2], [1.2, 1.2, 1.2], [1.1, 1.1, 1.1], [1.05, 1.05, 1.05]], 4,
                                    [microsoft, tesla, intel])
            oil_crisis_event = Event("Oil Crisis", [[0.85, 0.85], [0.85, 0.85], [0.95, 0.95]], 3, [bp, galp])
            tech_breakthrough_event = Event("Tech Breakthrough", [[1.3, 0.9, 0.9], [1.2, 1, 1]], 2,
                                            rd.sample([microsoft, tesla, intel], 3))
            positive_elon_tweet = Event("Positive Crazy Elon Musk Tweet",
                                        [[1.5, 1, 1, 1, 1, 1, 1, 1], [0.8, 1, 1, 1, 1, 1, 1, 1],
                                         [0.9, 1, 1, 1, 1, 1, 1, 1]], 3,
                                        rd.sample([bp, galp, primark, tesla, moderna, microsoft, aldi, intel], 8))
            negative_elon_tweet = Event("Negative Crazy Elon Musk Tweet",
                                        [[0.7, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                                         [1.1, 1, 1, 1, 1, 1, 1, 1]], 3,
                                        rd.sample([bp, galp, primark, tesla, moderna, microsoft, aldi, intel], 8))
            event_list = [covid_event, tech_breakthrough_event, tech_boom_event, oil_crisis_event, positive_elon_tweet,
                          negative_elon_tweet]
        return bank, event_list

    def get_random_agents(self):
        return self.random_agents_num

    def setup_agents(self):
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
            if self.game_mode == "DEFAULT":
                self.update_event()
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()
            # self.events.next().update()
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
            return (NoneEvent(1))
        else:
            return (rd.choice(self.events))

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
