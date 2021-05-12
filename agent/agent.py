import sys
from collections import defaultdict


class Agent:
    def __init__(self, central_bank, initialcash=1000):
        self.cash = initialcash
        self.cash_history = [initialcash]
        self.stock_history = [0]
        self.central_bank = central_bank
        # id stock : qtd owned
        self.stocks_owned = defaultdict(lambda: 0)  # when accessing a key not present adds that key with value 0

    def __repr__(self):
        return "Agent"

    # abstract method
    # agents will be able to use the following to make decisions
    # TO BUY
    # 1 - global news events
    # 2 - if share price is up or down
    # 3 - share price evolution throughout n rounds
    # 4 - dividends if we see it fit
    # Evaluate current portfolio
    #  - evaluate each share owned
    def __decide(self):
        pass

    def decide(self):
        self.__decide()
        self.__update_history()

    def buy(self, stock_id, qtd):
        cost = self.central_bank.stock_price(stock_id, qtd)
        if not self.__can_buy(cost):
            return
        if not self.central_bank.buy(stock_id, qtd):
            sys.stdout.write("failed to buy")
            sys.stdout.flush()
            return
        self.stocks_owned[stock_id] += qtd
        self.cash -= cost

    def sell(self, stock_id, qtd):
        if not self.__can_sell(stock_id, qtd):
            return
        value = self.central_bank.sell(stock_id, qtd)
        self.cash += value

    def __how_many_can_i_buy(self, stock_id):
        cost = self.central_bank.stock_price(stock_id, 1)
        return self.cash // cost

    def __buy_random_stock(self):  # should be part of random agent no?
        # TODO
        return 0

    def __can_buy(self, c):
        return self.cash >= c

    def __can_sell(self, id, qtd):
        return self.stocks_owned[id] >= qtd #if not present will be 0 >= qtd, and false, what we want

    def __get_owned_stocks_value(self):
        stock_value = 0
        for stock_id in self.stocks_owned:
            stock_value += self.central_bank.get_stock(stock_id).price * self.stocks_owned[stock_id]
        return stock_value

    def __update_history(self):
        self.stock_history.append(self.__get_owned_stocks_value())
        self.cash_history.append(self.cash)


class Random(Agent):
    type = "Random"

    def __decide(self):
        print(self.type + " decided!")
        self.__buy_random_stock()

    def __update_history(self):
        return


class GoldStandard(Agent):
    type = "GoldStandard"

    def __init__(self, central_bank, initialcash=1000):
        super().__init__(central_bank)
        self.current_step = 0

    def __decide(self):
        print(self.type + " decided!")
        if self.current_step != 0:
            return
        stocks = self.central_bank.get_all_stock()
        max_value_stock = max(stocks, key=lambda stock: stock.price)

        # buy as much as possible
        self.buy(max_value_stock.id, self.__how_many_can_i_buy(max_value_stock.id))

        return


class SimpleReactive(Agent):
    type = "SimpleReactive"
    # FIXME this number can be super different
    buy_qtd = 5

    def __decide(self):
        print(self.type + " decided!")

        # sell stock that has gone down
        for s in self.stocks_owned:
            if s.price_change < 1:
                self.sell(s.id, self.stocks_owned[s.id])

        # buy stock that has gone up
        all_stock = self.central_bank.get_all_stock()
        for s in all_stock:
            if s.price_change > 1:
                self.buy(s.id, self.buy_qtd)

        return


class Careful(Agent):
    type = "Careful"
    # FIXME this number can be super different
    buy_qtd = 5

    def __decide(self):
        print(self.type + " decided!")

        return
