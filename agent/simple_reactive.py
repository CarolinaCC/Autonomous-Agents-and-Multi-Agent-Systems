from agent.agent import Agent


class SimpleReactive(Agent):
    type = "SimpleReactive"
    # FIXME this number can be super different
    buy_qtd = 5

    def _decide(self):

        # react to global event TODO

        # sell stock that has gone down
        all_stock = self.central_bank.get_all_stock()
        for s in self.stocks_owned:
            if all_stock[s].get_latest_price_modifier() < 1.0:
                self.sell(s.id, self.stocks_owned[s.id])

        # buy stock that has gone up
        all_stock = self.central_bank.get_all_stock()
        for s in all_stock:
            # fixme
            if s.get_latest_price_modifier() > 1.0:
                self.buy(s.id, self.buy_qtd)

        return
