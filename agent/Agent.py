from CentralBank import CentralBank


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
        cost = CentralBank.value(id, qtd)
        if can_buy(cost):
            CentralBank.buy(id, qtd)
        self.cash -= cost

    def sell(self, id, qtd):
        if can_sell(cost):
            value = CentralBank.sell(id, qtd)
            self.cash += value


class Random(Agent):
    type = "Random"

    def decide(self):
        print(type + " decided!")
        return 0
