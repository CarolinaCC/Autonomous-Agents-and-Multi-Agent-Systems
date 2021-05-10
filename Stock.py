class Stock:
    def __init__(self, name, id, total_qtd, price):
        self.name = name
        self.id = id
        self.total_qtd = total_qtd
        self.av_qtd = total_qtd
        self.price = price

    def buy(self, qtd):
        self.av_qtd -= qtd

    def sell(self, qtd):
        self.av_qtd += qtd
