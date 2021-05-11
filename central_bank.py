from stock import Stock


class CentralBank:

    def __init__(self):
        self.current_step = 0
        self.stocks = []
        i = 0
        self.stocks.append(Stock("Enron", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("Galp", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("PencilFactory", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("Woodcutter", i, i * 2, i * 5, 1.5))

    def all_stock(self):
        return self.stocks

    def buy_stock(self, id: int, qtd: int):
        self.stocks[i].buy(qtd)
        return 0

    def sell_stock(self, id: int, qtd: int):
        self.stocks[i].sell(qtd)
        return 0

    def stock_price(self, id, qtd):
        return self.stocks[id].price * qtd

    def decide(self):
        self.current_step += 1
        for stock in self.stocks:
            self.__recalculate(stock)
        return 0

    def __recalculate(self, stock):
        # TODO
        stock.update_price(stock.price)
        return 0
