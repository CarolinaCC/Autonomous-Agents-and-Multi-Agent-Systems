class Stock:
    def __init__(self, name, stock_id, price, normal_modifier=0.00001, supply_modifier=0.00001):
        self.name = name
        self.id = stock_id
        self.price = price
        self.price_history = [price, price] #start with two entries so that get_current_step_value_change always works
        self.supply_change_history = [0]
        self.supply_change = 0
        self.normal_modifier = normal_modifier
        self.supply_modifier = supply_modifier

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
        self.price = price

    def apply_price_modifier(self, modifier):
        self.price *= modifier

    def apply_price_add(self, value):
        self.price += value

    def get_current_step_supply_change(self):
        return self.supply_change_history[-1]

    def get_current_step_price_change(self, current_step):
        return self.supply_change_history[-1] - self.supply_change_history[-2]

    def get_latest_price_modifier(self):
        l = len(self.price_history)
        if self.price_history[l - 2] <= 0:
            return 0
        res = self.price_history[l-1]/self.price_history[l-2]
        return res

    def recalculate_price(self):
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
        self.source_stock.apply_price_add(self.destination_stock.get_current_step_supply_change() * self.modifier)
        self.destination_stock.apply_price_add(self.source_stock.get_current_step_supply_change() * self.modifier)


