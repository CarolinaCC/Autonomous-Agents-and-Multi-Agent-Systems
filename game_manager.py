from CentralBank import CentralBank


class GameManager:
    event = False

    def __init__(self, random_agents_num, simple_react_agents_num, careful_react_agents_num, steps_num):
        self.random_agents_num = random_agents_num
        self.simple_react_agents_num = simple_react_agents_num
        self.careful_react_agents_num = careful_react_agents_num
        self.steps_num = steps_num
        self.central_bank = CentralBank()
        self.setup_agents()

    def setup_agents(self):
        for _ in range(self.random_agents_num):
            self.agents_array.append(Random())
        # FIXME adicionar novos agents
        for _ in range(self.simple_react_agents_num):
            self.agents_array.append(Random())
        for _ in range(self.careful_react_agents_num):
            self.agents_array.append(Random())

    def step(self, num_steps):
        for _ in range(num_steps):
            self.decideEvent()
            for a in self.agents_array:
                a.decide()
            central_bank.decide()

    def enable_event(self):
        self.event = True

    def decide_event(self):
        # TODO
        return
