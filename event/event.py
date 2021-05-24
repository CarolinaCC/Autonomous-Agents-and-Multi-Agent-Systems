# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/


class Event:
    def __init__(self, name, modifiers, num_steps, stocks=None):
        if stocks is None:
            stocks = []
        self.name = name
        self.modifiers = modifiers
        self.num_steps = num_steps
        self.stocks = stocks

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock, index):
        stock.update_price(self.modifiers[index] * stock.price)

    def update(self):
        for index, stock in enumerate(self.stocks):
            self.update_stock(stock, index)
        self.num_steps -= 1


class NoneEvent(Event):

    def __init__(self, num_steps=0):
        super().__init__("None", [0], num_steps, [])


class ElonMuskPositiveTweetEvent(Event):  # Uma companhia sobe bastante. Se calhar volta a descer rapidamente
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        # self.stocks_affected = Só quero que afecte uma stock, se calhar um one-hot array?
        # ou um nome de stock? Para isso preciso de ter lista dos nomes


class ElonMuskNegativeTweetEvent(Event):  # Uma companhia desce bastante. Se calhar volta a subir rapidamente
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        # self.stocks_affected = Só quero que afecte uma stock, se calhar um one-hot array?
        # ou um nome de stock? Para isso preciso de ter lista dos nomes


class GlobalPandemicEvent(Event):  # Quase todas as companhias descem. Umas poucas sobem (farmacêuticas)
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)


class TechBreakthroughEvent(Event):  # Uma companhia sobe e companhias rivais descem
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)


class WarrenBuffetListEvent(Event):  # Warren Buffet invests in a list of stocks and they go up
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)


class IlegalMonopolyFineEvent(Event):  # 2+ companies are fined for having illegal monopoly (ou entao concorrencia
    # desleal) and their shares drop somewhat
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)


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
