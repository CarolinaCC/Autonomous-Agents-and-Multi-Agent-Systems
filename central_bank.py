from stock import Stock


class CentralBank:
    SUPPLY_DEMAND_FACTOR = 1.1
    STOCK_COMPLEMENTARY_FACTOR = 1.03
    STOCK_COMPETITIVE_FACTOR = 1.03

    def __init__(self):
        self.current_step = 0
        self.stocks = []
        i = 0
        self.stocks.append(Stock("Enron", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("Galp", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("PencilFactory", i, i * 2, i * 5, 1.5))
        i += 1
        self.stocks.append(Stock("Woodcutter", i, i * 2, i * 5, 1.5))

        self.complementary_stocks = {stock: [] for stock in self.stocks}  # todo preencer
        # se calhar seria mais simples ter uma classe que representa uma relação entre dois stocks
        # e depois uma lista dessas classes
        self.competitive_stocks = {stock: [] for stock in self.stocks}  # todo preencer

    def get_all_stock(self):
        return self.stocks

    def buy_stock(self, id: int, qtd: int):
        self.stocks[id].buy(qtd, self.current_step)
        return 0

    def sell_stock(self, id: int, qtd: int):
        self.stocks[id].sell(qtd, self.current_step)
        return 0

    def stock_price(self, id, qtd):
        return self.stocks[id].price * qtd

    def decide(self, current_step):
        for stock in self.stocks:
            self.__recalculate(stock, current_step)
        return 0

    def get_stock(self, stock_id):
        return self.stocks[stock_id]

    def get_dividends(self, id):
        # https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/
        return self.stocks[id]

    def __recalculate(self, stock, current_step):
        # TODO
        # The stock prices can be affected by:
        # 1 - stock.modifier
        # 2 - law of supply and demand
        # 3 - global news events
        # 4 - complementary industries
        # 5 - competitor industries

        # stock modifier
        stock.update_price(stock.price * stock.modifier, current_step)

        # law of supply and demand: If in the current step
        # there where more buys then sells, the price increases, otherwise it decreases
        # by a constant factor each turn
        if stock.was_demand_greater_than_supply(current_step):
            stock.update_price(stock.price * CentralBank.SUPPLY_DEMAND_FACTOR, current_step)
        else:
            stock.update_price(stock.price / CentralBank.SUPPLY_DEMAND_FACTOR, current_step)

        # TODO este metodo recebe um evento e aplica o evento à stock

        # check complementary stocks
        complementary_modifier = 1
        for complementary_stock in self.complementary_stocks[stock]:
            if complementary_stock.has_value_risen_in_step(current_step):
                complementary_modifier *= CentralBank.STOCK_COMPLEMENTARY_FACTOR
            else:
                complementary_modifier /= CentralBank.STOCK_COMPLEMENTARY_FACTOR
        stock.update_price(stock.price * complementary_modifier, current_step)

        # check competitive stocks
        competitive_modifier = 1
        for complementary_stock in self.complementary_stocks[stock]:
            if complementary_stock.has_value_risen_in_step(current_step):
                competitive_modifier /= CentralBank.STOCK_COMPETITIVE_FACTOR
            else:
                competitive_modifier *= CentralBank.STOCK_COMPETITIVE_FACTOR
        stock.update_price(stock.price * competitive_modifier, current_step)
