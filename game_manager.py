from CentralBank import CentralBank

class GameManager:

    def __init__(self, random_agents_num, reactive_agents_num, steps_num):
        self.random_agents_num = random_agents_num
        self.reactive_agents_num = reactive_agents_num
        self.steps_num = steps_num
        self.central_bank = CentralBank()
        # self.agents_array = AGENTS ARRAY (SETUP)

        #
        #
        # array {nome : random_agents_1, saldo : 10000, }

    def setup():
        # TODO receive info about runs... agents
        # for type in agents_type:
        agents.append(Random())

    def run():
        # receive info about run from optionMenu
        for _ in range(runs):
            step()
        # TODO call a aos eventos

    #recebe num de steps
    def step():
        for a in agents:
            a.decide()
        central_bank.decide()