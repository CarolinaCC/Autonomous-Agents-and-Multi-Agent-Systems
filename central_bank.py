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

    def get_all_stock(self):
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

    def get_stock(self, id):
        return self.stocks[i]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[i]

    def __recalculate(self, stock):
        # TODO
        # The stock prices can be affected by:
        # 1 - stock.modifier
        # 2 - law of supply and demand
        # 3 - global news events
        # 4 - complementary industries
        # 5 - competitor industries

        stock.update_price(stock.price*stock.modifier)
        return 0
