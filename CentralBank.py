import sys
from Stock import Stock

class CentralBank:
    stocks = []

    def __init__(self):
        for i in range(0, 10):
            self.stocks.append(Stock("", i, i * 2, i * 5))

    def all_stock(self):
        return stocks

    def buy_stock(self, id: int, qtd: int):
        stocks[i].buy(qtd)
        return 0

    def sell_stock(self, id: int, qtd: int):
        stocks[i].sell(qtd)
        return 0

    def value(self, id, qtd):
        return stocks[id].price * qtd

    def decide(self):
        return 0

    def recalculate(self):
        return 0
