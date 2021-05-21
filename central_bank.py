from stock import Stock, StockRelation


class CentralBank:
    def __init__(self):
        self.current_step = 0
        self.stocks = []
        self.stock_relations = []

        i = 0
        enron = Stock("Enron", i, i * 2, i * 5, 1.5)
        self.stocks.append(enron)
        i += 1
        galp = Stock("Galp", i, i * 2, i * 5, 1.5)
        self.stocks.append(galp)
        i += 1
        pencil_factory = Stock("PencilFactory", i, i * 2, i * 5, 1.5)
        self.stocks.append(pencil_factory)
        i += 1
        woodcutter = Stock("Woodcutter", i, i * 2, i * 5, 1.5)
        self.stocks.append(woodcutter)

        self.stock_relations.append(StockRelation(enron, galp, -0.001))
        self.stock_relations.append(StockRelation(pencil_factory, woodcutter, 0.001))


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

    def decide(self, current_event):
        for stock in self.stocks:
            stock.recalculate_price()
        for stock in self.stocks:
            stock.update_history()
        for relation in self.stock_relations:
            relation.update()

        current_event.update(self.stocks)

        return 0

    def get_stock(self, stock_id):
        return self.stocks[stock_id]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[id]
