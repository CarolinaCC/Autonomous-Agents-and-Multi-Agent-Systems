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

        self.complementary_stocks = {stock: [] for stock in self.stocks} # todo preencer
        # se calhar seria mais simples ter uma classe que representa uma relação entre dois stocks
        # e depois uma lista dessas classes
        self.competitive_stocks = {stock: [] for stock in self.stocks} # todo preencer

    def get_all_stock(self):
        return self.stocks

    def buy_stock(self, id: int, qtd: int):
        self.stocks[id].buy(qtd)
        return 0

    def sell_stock(self, id: int, qtd: int):
        self.stocks[id].sell(qtd)
        return 0

    def stock_price(self, id, qtd):
        return self.stocks[id].price * qtd

    def decide(self):
        for stock in self.stocks:
            stock.recalculate_price()
        for stock in self.stocks:
            stock.update_history()

        return 0

    def get_stock(self, stock_id):
        return self.stocks[stock_id]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[id]