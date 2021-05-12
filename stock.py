import json

class Stock:
    def __init__(self, name, id, total_qtd, price, modifier):
        self.name = name
        self.id = id
        self.total_qtd = total_qtd
        self.av_qtd = total_qtd
        self.price = price
        self.modifier = modifier
        self.history = [price]
        self.current_step = 0
        self.price_change = 0.0

    def buy(self, qtd):
        self.av_qtd -= qtd

    def sell(self, qtd):
        self.av_qtd += qtd

    def __repr__(self):
        out = str(self.id) + " " + self.name
        for s in self.history:
            out += " " + str(s)
        out += "\n"
        return out

    def update_price(self, price):
        self.current_step += 1
        self.price = price
        self.history.append(price)
        self.price_change = price / self.history[self.current_step-1]


