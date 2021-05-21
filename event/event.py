# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/

class Event:
    def __init__(self, name, modifier):
        self.name = name
        self.modifier = modifier

    # returns True if the event applies to the stock, False otherwise
    def applies_to_stock(self, stock):
        pass

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock, current_step):
        if (self.applies_to_stock(stock)):
            stock.update_price(self.modifier * stock.price, current_step)

class NoneEvent:
    def applies_to_stock(self):
        return False
