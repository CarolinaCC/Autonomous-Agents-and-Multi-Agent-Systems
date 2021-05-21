import json
from collections import defaultdict


class Stock:
    def __init__(self, name, stock_id, price, modifier, i_dont_know):
        self.name = name
        self.id = stock_id
        self.price = price
        self.modifier = modifier
        self.history_price = [price]
        self.history_quantity = defaultdict(lambda: 0)  # when accessing a key not present adds that key with value 0
        self.current_step = 0
        self.price_change = 0.0

    def buy(self, qtd, current_step):
        # TODO fazer uma ronda 0 inicial para não ter estes -1 :(
        self.history_quantity[current_step + 1] += qtd
        return

    def sell(self, qtd, current_step):
        self.history_quantity[current_step + 1] -= qtd
        return

    def __repr__(self):
        out = str(self.id) + " " + self.name
        for s in self.history_price:
            out += " " + str(s)
        out += "\n"
        return out

    def update_price(self, price, current_step):
        self.price = price
        self.history_price.append(price)
        if self.history_price[current_step + 1] != 0:
            self.price_change = price / self.history_price[current_step + 1]
