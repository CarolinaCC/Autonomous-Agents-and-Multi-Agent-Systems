from agent.agent import Agent

class GoldStandard(Agent):
    type = "GoldStandard"

    def __init__(self, central_bank, initial_cash=1000):
        super().__init__(central_bank)
        self.current_step = 0

    def _decide(self):
        if self.current_step != 0:
            return
        stocks = self.central_bank.get_all_stock()
        max_value_stock = max(stocks, key=lambda stock: stock.price)

        # buy as much as possible
        self.buy(max_value_stock.id, self._Agent__how_many_can_i_buy(max_value_stock.id))

        return