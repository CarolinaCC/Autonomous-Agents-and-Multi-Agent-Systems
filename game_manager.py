from central_bank import CentralBank
from agent.agent import *
from agent.gold_standard import *
from agent.simple_reactive import *
import os
import sys

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
        self.current_step = 0
        self.game_mode = 'GAME_MODE_TO_DO'
        self.end_flag = False

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
        for current_step in range(num_steps):
            if self.current_step >= self.steps_num:
                self.end_flag = True
                return
            sys.stdout.write(str(self.current_step))
            sys.stdout.flush()
            self.decide_event()
            # TODO criar os eventos e passa-los para o decide para se poder usar no reecalculate
            for a in self.agents_array:
                a.decide()
            self.central_bank.decide()

    def enable_event(self):
        self.event = True

    def decide_event(self):
        # TODO
        return

    def get_current_event(self):
        # TODO
        return 'CURRENT_EVENT'

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
