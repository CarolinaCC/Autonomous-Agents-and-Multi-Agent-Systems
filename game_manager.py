from central_bank import CentralBank
from agent.agent import *
import os
import json


class GameManager:
    event = False

    def __init__(self, random_agents_num, simple_react_agents_num, careful_react_agents_num, steps_num):
        self.random_agents_num = random_agents_num
        self.simple_react_agents_num = simple_react_agents_num
        self.careful_react_agents_num = careful_react_agents_num
        self.steps_num = steps_num
        self.central_bank = CentralBank()
        self.agents_array = []
        self.setup_agents()

    def setup_agents(self):
        for _ in range(self.random_agents_num):
            self.agents_array.append(Random(self.central_bank))
        # FIXME adicionar novos agents
        for _ in range(self.simple_react_agents_num):
            self.agents_array.append(Random(self.central_bank))
        for _ in range(self.careful_react_agents_num):
            self.agents_array.append(Random(self.central_bank))

    def step(self, num_steps):
        for _ in range(num_steps):
            self.decide_event()
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()

    def enable_event(self):
        self.event = True

    def decide_event(self):
        # TODO
        return

    def print_results(self):
        i = 0
        # FIXME
        while os.path.exists("outputs/stock_history" + str(i) + ".json"):
            i += 1
        with open("outputs/stock_history" + str(i) + ".txt", 'w', encoding='utf-8') as f:
            for stock in self.central_bank.stocks:
                f.write(repr(stock))
            #     json.dump(stock.toJSON(), f, ensure_ascii=False, indent=4)
        f.close()

        # with open("agent_history" + str(i) + ".txt", 'w', encoding='utf-8') as f:
        #     for a in self.agents_array:
        #         json.dump(a, f, ensure_ascii=False, indent=4)
        f.close()