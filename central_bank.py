from stock import Stock, StockRelation


class CentralBank:
    def __init__(self):
        self.current_step = 0
        self.stocks = []
        self.stock_relations = []

        enron = Stock("Enron", 0, 1.6, 1.01, 0.002)
        self.stocks.append(enron)
        galp = Stock("Galp", 1, 2.9, 1.02, 0.003)
        self.stocks.append(galp)
        primark = Stock("Primark", 2, 2.2, 1.025, 0.006)
        self.stocks.append(primark)
        tesla = Stock("Tesla", 3, 3.1, 1.05, 0.001)
        self.stocks.append(tesla)
        apple = Stock("Apple", 4, 3.3, 1.01, 0.002)
        self.stocks.append(apple)
        microsoft = Stock("Microsoft", 5, 2.2, 1.02, 0.003)
        self.stocks.append(microsoft)
        aldi = Stock("Aldi", 6, 4.1, 1.025, 0.006)
        self.stocks.append(aldi)
        intel = Stock("Intel", 7, 3.1, 1.05, 0.001)
        self.stocks.append(intel)

        self.stock_relations.append(StockRelation(enron, galp, -0.00009))
        self.stock_relations.append(StockRelation(primark, aldi, -0.00007))
        self.stock_relations.append(StockRelation(tesla, intel, 0.00005))
        self.stock_relations.append(StockRelation(microsoft, intel, 0.00003))

    def get_all_stock(self):
        return self.stocks

    def buy_stock(self, id: int, qtd: int):
        self.stocks[id].buy(qtd)
        return True

    def sell_stock(self, id: int, qtd: int):
        self.stocks[id].sell(qtd)
        return True

    def stock_price(self, id, qtd):
        return self.stocks[id].price * qtd

    def decide(self):
        for stock in self.stocks:
            stock.recalculate_price()
        for stock in self.stocks:
            stock.update_history()
        for relation in self.stock_relations:
            relation.update()
        return 0

    def get_stock(self, stock_id):
        return self.stocks[stock_id]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[id]
