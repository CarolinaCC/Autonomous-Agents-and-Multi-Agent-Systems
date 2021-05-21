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

    def was_demand_greater_than_supply(self, current_step):
        return self.history_quantity[current_step + 1] > 0

    def has_value_risen_in_step(self, current_step):
        return self.history_price[current_step + 1] > self.history_price[current_step]


# Defines a relation between two stocks.
# If the value of source_stock increases in a step
# then the value of destination stock should be multiplied by the modifier and vice versa.
# If the value of source_stock decreases in a step
# then the value of destination stock should be divided by the modifier and vice versa.
# Que achas desta classe?
class StockRelation:
    def __init__(self, source_stock, destination_stock, modifier):
        self.source_stock = source_stock
        self.destination_stock = destination_stock
        self.modifier = modifier

    def apply(self, current_step):
        if (self.source_stock.has_value_risen_in_step(current_step)):
            self.destination_stock.update_price(self.modifier * self.destination_stock.price)
        else:
            self.destination_stock.update_price(self.modifier / self.destination_stock.price)
        if (self.destination_stock.has_value_risen_in_step(current_step)):
            self.source_stock.update_price(self.modifier * self.source_stock.price)
        else:
            self.source_stock.update_price(self.modifier / self.source_stock.price)

