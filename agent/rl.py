import random
from math import exp

from agent.agent import Agent


class ReinforcementLearning(Agent):
    type = "RL"

    '''
    q(state, action)
    The states are:
        Each combination of owning stocks: 2 exp 10 stocks 
    
    The actions are:
        3 for each stock: buy, sell
        10 stocks
        
    The matrix is going to be 100x30
    
            c1 v1 c2 v2 c3 v3 c4 v4 n
        s1  0  0  0  0  0  0  0  0  0
        s2  0  0  0  0  0  0  0  0  0
        s3  0  0  0  0  0  0  0  0  0
    '''

    def __init__(self, central_bank, initial_cash=1000, soft_max=False):
        super().__init__(central_bank, initial_cash)
        self.current_step = 0
        self.q = []
        self.discount = 0.9
        self.total = 1000000
        self.learningRate = 0.8
        self.epsilon = 0.9
        self.rand_factor = 0.05
        self.reward_modifier = 100
        self.init_q_values()
        self.original_state = 0
        self.original_action = 0
        self.dec = (self.epsilon - 0.1) / self.total
        self.soft_max = soft_max

    def init_q_values(self):
        num_col = 2 * len(self.central_bank.get_all_stock())
        num_lines = 2 ** len(self.central_bank.get_all_stock())

        for i in range(num_lines):
            tmp = [0 for _ in range(num_col)]
            # tmp.append(0)
            self.q.append(tmp)

    def get_state(self):
        l = len(self.central_bank.get_all_stock())
        owned_stocks = set(self.stocks_owned.keys())
        s = "".join(["0" if i in owned_stocks else "1" for i in range(l)])
        return int(s, 2)

    def learn(self):
        u = self.reward()
        prev_q = self.get_q(self.original_state, self.original_action)
        self.epsilon = max(self.epsilon - self.dec, 0.05)

        '''
        Q-function update
        '''
        pred_error = u + self.discount * self.get_max_q(self.get_state()) - prev_q

        new_q = prev_q + (self.learningRate * pred_error)
        self.q[self.original_state][self.original_action] = new_q
        return

    def _decide(self):
        self.original_state = self.get_state()
        self.epsilon -= self.dec
        act = 0
        if random.uniform(0, 1) < self.rand_factor:
            act = self.do_random_action(self.get_available_actions())
        else:
            if self.soft_max:
                act = self.do_soft_max()
            else:
                act = self.do_e_greedy()
        self.original_action = act

    def get_available_actions(self):
        owned_stocks = set(self.stocks_owned.keys())
        l = len(self.central_bank.get_all_stock())

        buy_actions = [2 * i for i in range(l) if self.central_bank.stocks[i].price <= self.cash]
        sell_actions = [2 * i + 1 for i in range(l) if i in owned_stocks]

        return [*buy_actions, *sell_actions]

    def do_e_greedy(self):
        valid_actions = self.get_available_actions()
        if random.uniform(0, 1) < self.rand_factor:
            return self.do_random_action(valid_actions)
        state = self.get_state()
        act = self.get_max_action_q(state, valid_actions)
        self.do_action(act)
        return act

    def do_soft_max(self):
        valid_actions = self.get_available_actions()
        act = -1
        l = len(valid_actions)
        tmp = self.get_q(self.get_state(), 0) / (self.epsilon * 100.0)
        if tmp != 0:
            cumulative = [exp(tmp)]
        else:
            cumulative = [0.0]
        for i in range(1, l):
            tmp = self.get_q(self.get_state(), 0) / (self.epsilon * 100.0)
            cumulative.append(exp(tmp) + cumulative[i - 1])
        total = cumulative[l - 1]
        cut = random.random() * total
        for i in range(l):
            if cut <= cumulative[i]:
                act = valid_actions[i]
                break
        if act >= 0:
            self.do_action(act)
        return act

    def get_random_available_action(self):
        valid_actions = self.get_available_actions()
        action = valid_actions[random.randint(0, len(valid_actions) - 1)]
        return action

    def do_random_action(self, valid_actions):
        action = valid_actions[random.randint(0, len(valid_actions) - 1)]
        self.do_action(action)
        return action

    def do_action(self, action):
        #if action == len(self.q[0])-1:
         #   return
        stock_id = action // 2
        if action % 2:
            #  odd, means sell
            max_sell = self.how_many_can_i_sell(stock_id)
            to_sell = random.randint(0, max_sell)
            self.sell(stock_id, to_sell)
            # print("sell: " + str(stock_id) + " quantity: " + str(to_sell))
        else:
            # even, means buy
            max_buy = self.how_many_can_i_buy(stock_id) - 1
            to_buy = random.randint(0, max_buy)
            self.buy(stock_id, to_buy)
            # print("buy: " + str(stock_id) + " quantity: " + str(to_buy) )

    def reward(self):
        l = len(self.stock_history)
        current_value = self.value_history[- 1]
        pre_value = self.value_history[- 2]

        r = current_value - pre_value
        #print(str(r))

        return r

    def get_q(self, original_state, original_action):
        return self.q[original_state][original_action]

    def get_max_q(self, state):
        return max(self.q[state])

    def get_max_action_q(self, state, valid_actions):
        max = float("-inf")
        max_i = -1
        line = self.q[state]
        for i in range(len(valid_actions)):
            q_action = line[valid_actions[i]]
            if q_action > max:
                max = q_action
                max_i = valid_actions[i]
        return max_i
