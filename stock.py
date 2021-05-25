class Stock:
    def __init__(self, name, stock_id, price, normal_modifier=0.00001, supply_modifier=0.00001, min_price=0.01,
                 mode="DEFAULT"):
        self.name = name
        self.id = stock_id
        self.price = price
        self.min_price = min_price
        self.price_history = [price, price]  # start with two entries so that get_current_step_value_change always works
        self.supply_change_history = [0]
        self.supply_change = 0
        self.normal_modifier = normal_modifier
        self.supply_modifier = supply_modifier
        self.game_mode = mode

    def buy(self, quantity):
        self.supply_change += quantity
        return

    def sell(self, quantity):
        self.supply_change -= quantity
        return

    def update_history(self):
        self.price_history.append(self.price)
        self.supply_change_history.append(self.supply_change)
        self.supply_change = 0

    def __repr__(self):
        return " ".join([str(self.id), self.name, *(str(price) for price in self.price_history)])

    def update_price(self, price):
        self.price = max(price, self.min_price)

    def apply_price_modifier(self, modifier):
        if self.price >= 0:
            self.price *= modifier
        else:
            # prevent snowball effect
            self.price /= modifier
        self.update_price(self.price)

    def apply_price_add(self, value):
        self.price += value
        self.update_price(self.price)

    def get_current_step_supply_change(self):
        return self.supply_change_history[-1]

    def get_current_step_price_change(self):
        return self.price_history[-1] - self.price_history[-2]

    # Returns variation in percentage (0-1)
    def get_latest_price_modifier(self):
        l = len(self.price_history)
        if self.price_history[l - 2] <= 0:
            return 0
        res = self.price_history[l - 1] / self.price_history[l - 2]

        return res

    # Returns variation in percentage (0-100%)
    def get_percentage_variation(self):
        l = len(self.price_history)
        if self.price_history[l - 2] == 0:
            return 0
        res = (self.price_history[l - 1] - self.price_history[l - 2]) / abs(self.price_history[l - 2]) * 100
        return res

    def get_price_chance_in_rounds(self, rounds):
        l = len(self.price_history)
        if l < rounds:
            return 0
        if self.price_history[l - 1 - rounds] <= 0:
            return 0
        value = float("-inf")
        for i in range(l-rounds, l):
            if self.price_history[i] < value:
                return 0
            value = self.price_history[i]
        return 2

    def recalculate_price(self):
        if self.game_mode == "RECESSION":
            if self.normal_modifier <= 1:
                self.apply_price_modifier(self.normal_modifier)
                return
            else:
                self.normal_modifier = 1/self.normal_modifier
                self.apply_price_modifier(self.normal_modifier)
                return

        elif self.game_mode == "INFLATION":
            if self.normal_modifier > 1:
                self.apply_price_modifier(self.normal_modifier)
                return
            else:
                self.normal_modifier += 1
                self.apply_price_modifier(self.normal_modifier)
                return

        else:

            # 1 - stock.modifier
            self.apply_price_modifier(self.normal_modifier)
            # 2 - law of supply and demand
            self.apply_price_add(self.get_current_step_supply_change() * self.supply_modifier)


'''
Represents a relation between stocks.
The value of the source_stock increased by 
value modifier* delta of value of destination_stock
every step and vice versa
Modifier should be negative for competitive stocks
and positive for complementary stocks
'''


class StockRelation:
    def __init__(self, source_stock, destination_stock, modifier):
        self.source_stock = source_stock
        self.destination_stock = destination_stock
        self.modifier = modifier

    def update(self):
        self.source_stock.apply_price_add(self.destination_stock.get_current_step_price_change() * self.modifier)
        self.destination_stock.apply_price_add(self.source_stock.get_current_step_price_change() * self.modifier)
