# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
import random as rd


class Event:
    def __init__(self, name, modifier, num_steps, stocks=None):
        if stocks is None:
            stocks = []
        self.name = name
        self.modifier = modifier  # List of lists with the modifiers for each step. Len must be = num_steps
        self.num_steps = num_steps
        self.stocks = stocks

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock):
        stock.update_price(self.modifier * stock.price)

    def update(self):
        for stock in self.stocks:
            self.update_stock(stock)
        self.num_steps -= 1


class NoneEvent(Event):

    def __init__(self, num_steps=0):
        super().__init__("None", [0], num_steps, [])


class EventIterator:

    def __init__(self, events):
        self.events = events
        self.i = 0
        self.none_event = NoneEvent(1)

    def next(self):
        if self.i == len(self.events):
            return self.none_event

        ret = self.events[self.i]
        if ret.num_steps == 0:
            self.i += 1
            return self.next()

        return ret
