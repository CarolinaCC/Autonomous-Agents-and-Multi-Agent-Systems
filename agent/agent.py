class Agent:
    def __init__(self, central_bank, initialcash=1000):
        self.cash = initialcash
        self.central_bank = central_bank
        self.stocks_owned = []

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
        cost = self.central_bank.stock_price(id, qtd)
        if not can_buy(cost):
            return
        if not self.central_bank.buy(id, qtd):
            return
        # TODO adicionar a stock
        self.cash -= cost

    def sell(self, id, qtd):
        if not can_sell(cost):
            return
        value = self.central_bank.sell(id, qtd)
        self.cash += value

    def __how_many_can_i_buy(self, id):
        cost = self.central_bank.stock_price(id, 1)
        return self.cash // cost


class Random(Agent):
    type = "Random"

    def decide(self):
        print(self.type + " decided!")
        return 0


class GoldStandard(Agent):
    type = "GoldStandard"

    def decide(self):
        print(self.type + " decided!")
        if self.current_step != 0:
            return
        else:
            stocks = self.central_bank.all_stock()
            max_value_stock = stocks[0]
            for s in stocks:
                max_value_stock = s if s.price > max_value_stock.price else max_value_stock

        # buy as much as possible
        self.buy(max_value_stock.id, self.__how_many_can_i_buy(max_value_stock.id))
        return


class SimpleReactive(Agent):
    type = "SimpleReactive"

    def decide(self):
        print(self.type + " decided!")
        if self.current_step != 0:
            return
        else:
            stocks = self.central_bank.all_stock()
            max_value_stock = stocks[0]
            for s in stocks:
                max_value_stock = s if s.price > max_value_stock.price else max_value_stock

        # buy as much as possible
        cost = self.central_bank.stock_price(max_value_stock.id, 1)
        number_to_buy = self.cash // cost
        self.buy(max_value_stock.id, number_to_buy)
        return