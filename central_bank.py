from stock import Stock, StockRelation


class CentralBank:
    def __init__(self, stocks=None, stock_relations=None, mode="DEFAULT"):
        if stock_relations is None:
            stock_relations = []
        if stocks is None:
            stocks = []
        self.mode = mode
        self.current_step = 0
        self.stocks = stocks
        self.stock_relations = stock_relations

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
        if "DEFAULT" in self.mode:
            for relation in self.stock_relations:
                relation.update()
        return 0

    def get_stock(self, stock_id):
        return self.stocks[stock_id]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[id]
