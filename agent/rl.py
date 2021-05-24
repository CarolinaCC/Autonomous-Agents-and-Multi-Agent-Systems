import random

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
    
            c1 v1 c2 v2 c3 v3 c4 v4
        s1  0  0  0  0  0  0  0  0 
        s2  0  0  0  0  0  0  0  0 
        s3  0  0  0  0  0  0  0  0 
    '''

    ## state action
    ## we can

    def __init__(self, central_bank, initial_cash=1000):
        super().__init__(central_bank, initial_cash)
        self.current_step = 0
        self.dec = (self.epsilon - 0.1) / self.total
        self.q = []
        self.discount = 0.9
        self.total = 1000000
        self.learningRate = 0.8
        self.epsilon = 0.9
        self.rand_factor = 0.05
        self.init_q_values()

    def init_q_values(self):
        num_lines = 2 * len(self.central_bank.get_all_stock())
        num_col = 2 ** len(self.central_bank.get_all_stock())

        for i in range(num_lines):
            tmp = [0 for _ in range(num_col)]
            self.q.append(tmp)

    def get_state(self):
        l = len(self.central_bank.get_all_stock())
        owned_stocks = set(self.stocks_owned.keys())
        s = "".join(["0" if i in owned_stocks else "1" for i in range(l)])
        return int(s, 2)

    def _decide(self):
        original_state = 0
        original_action = 0
        u = self.reward(original_state, original_action)

        prev_q = self.get_q(original_state, original_action)

        pred_error = 0

        epsilon = max(self.epsilon - self.dec, 0.05)
        # ahead = aheadPosition(); // percept

        pred_error = u + self.discount * self.get_max_q(self.get_state()) - prev_q

        # self.set_q(originalState, originalAction, prevq + (learningRate * predError));
        return

    def action(self):
        self.epsilon -= self.dec
        if random.uniform(0, 1) < self.rand_factor:
            self.random_action()
        else:
            act = random.randint(0, 2 * len(self.central_bank.get_all_stock()))

    def reward(self, original_state, original_action):
        return 0

    def get_q(self, original_state, original_action):
        return 0

        '''
        ABC
        000   - 0
        001   - 1  
        010   - 2
        '''

    def get_max_q(self, param):
        return 0

    def random_action(self):
        pass
