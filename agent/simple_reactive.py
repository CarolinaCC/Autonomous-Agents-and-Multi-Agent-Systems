from agent.agent import Agent

class SimpleReactive(Agent):
    type = "SimpleReactive"
    # FIXME this number can be super different
    buy_qtd = 5

    def _decide(self):
        print(self.type + " decided!")

        # react to global event TODO

        # sell stock that has gone down
        for s in self.stocks_owned:
            if s.price_change < 1:
                self.sell(s.id, self.stocks_owned[s.id])

        # buy stock that has gone up
        all_stock = self.central_bank.get_all_stock()
        for s in all_stock:
            if s.price_change > 1:
                self.buy(s.id, self.buy_qtd)

        return