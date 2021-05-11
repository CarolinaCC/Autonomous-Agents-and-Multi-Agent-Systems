from CentralBank import CentralBank
from Main import central_bank


class Agent:
    def __init__(self, initialcash=None):
        if initialcash is None:
            self.cash = 1000
        self.cash = initialcash

    def __repr__(self):
        return "Agent"

    # abstract method
    def decide(self):
        pass

    def can_buy(self, c):
        return self.cash >= c

    def can_sell(self, id, qtd):
        # TODO
        return self.cash >= c

    def buy(self, id, qtd):
        cost = central_bank.value(id, qtd)
        if not can_buy(cost):
            return
        if not central_bank.buy(id, qtd):
            return
        # TODO adicionar a stock
        self.cash -= cost

    def sell(self, id, qtd):
        if not can_sell(cost):
            return
        value = central_bank.sell(id, qtd)
        self.cash += value


class Random(Agent):
    type = "Random"

    def decide(self):
        print(self.type + " decided!")
        return 0
