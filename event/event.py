# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/


class Event:
    def __init__(self, name, modifier, num_steps):
        self.name = name
        self.modifier = modifier
        self.num_steps = num_steps

    # returns True if the event applies to the stock, False otherwise
    def applies_to_stock(self, stock):
        pass

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock):
        if self.applies_to_stock(stock):
            stock.update_price(self.modifier * stock.price)

    def update(self, stocks):
        for stock in stocks:
            self.update_stock(stock)
        self.num_steps -= 1

class NoneEvent:
    def applies_to_stock(self):
        return False

class EventIterator:
    def __init__(self, events):
        self.events = events
        self.i = 0
        self.none = NoneEvent()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.i >= len(self.events):
            return self.none
        if self.events[self.i].num_steps == 0:
            self.i += 1
            return self.next()
        return self.events[self.i]

