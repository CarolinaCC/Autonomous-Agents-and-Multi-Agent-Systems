# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
import random as rd


class Event:
    def __init__(self, name, modifiers, num_steps, stocks=None):
        if stocks is None:
            stocks = []
        self.name = name
        self.modifiers = modifiers  # List of lists with the modifiers for each step. Len must be = num_steps
        self.num_steps = num_steps
        self.stocks = stocks
        self.curr_step = 0
        self.is_over = False

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock, index):
        stock.update_price(self.modifiers[self.curr_step][index] * stock.price)

    def update(self):
        for index, stock in enumerate(self.stocks):
            self.update_stock(stock, index)
        self.curr_step += 1
        if self.curr_step >= self.num_steps:
            self.is_over = True

    def reset(self):
        self.curr_step = 0
        self.is_over = False
        self.stocks = rd.sample(self.stocks, len(self.stocks))


class NoneEvent(Event):

    def __init__(self, num_steps=0):
        super().__init__("None", [0], num_steps, [])

    def update(self):
        self.curr_step += 1
        if self.curr_step >= self.num_steps:
            self.is_over = True


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


class WarrenBuffetListEvent(Event):  # Warren Buffet invests in a list of stocks and they go up
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)


class IlegalMonopolyFineEvent(Event):  # 2+ companies are fined for having illegal monopoly (ou entao concorrencia
    # desleal) and their shares drop somewhat
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
