import random

from agent.agent import Agent


class Careful(Agent):
    type = "Careful"
    # number of round it sees an increase in order for it qualify as a trend
    rounds_before_trend = 4

    def _decide(self):
        # sell stock that has gone down
        all_stock = self.central_bank.get_all_stock()
        for id, s in self.stocks_owned.items():
            if all_stock[id].get_latest_price_modifier() < 1.0:
                self.sell(id, self.stocks_owned[id])

        # buy stock that has gone up across rounds
        all_stock = self.central_bank.get_all_stock()

        for s in all_stock:
            if s.get_price_chance_in_rounds(self.rounds_before_trend) > 1.000001:
                amount_to_buy = self.how_many_can_i_buy(s.id)
                if amount_to_buy > 0:
                    amount_to_buy = random.randint(1, amount_to_buy)
                    self.buy(s.id, amount_to_buy)
        return
