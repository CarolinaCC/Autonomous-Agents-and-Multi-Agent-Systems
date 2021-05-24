import random


from agent.agent import Agent


class SimpleReactive(Agent):
    type = "SimpleReactive"
    # FIXME this number can be super different
    buy_qtd = 5

    def _decide(self):

        # react to global event TODO

        # sell stock that has gone down
        all_stock = self.central_bank.get_all_stock()
        for id, s in self.stocks_owned.items():
            if all_stock[id].get_latest_price_modifier() < 1.0:
                self.sell(id, self.stocks_owned[id])

        # buy stock that has gone up
        all_stock = self.central_bank.get_all_stock()
        for s in all_stock:
            if s.get_latest_price_modifier() > 1.0:
                amount_to_buy = self.how_many_can_i_buy(s.id)

                if amount_to_buy > 0:
                    amount_to_buy = random.randint(1, amount_to_buy)
                    self.buy(s.id, amount_to_buy)

        return
