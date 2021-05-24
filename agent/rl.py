from agent.agent import Agent


class ReinforcementLearning(Agent):
    type = "RL"
    discount = 0.9
    learningRate = 0.8
    epsilon = 0.9
    rand_factor = 0.05
    '''
    q(state, action)
    The states are:
        Each combination of owning stocks: 2 exp 10 stocks 
    
    The actions are:
        3 for each stock: buy, sell, hold (no nothing)
        10 stocks
        
    The matrix is going to be 100x30
    
    '''
    q = [[], []]

    def __init__(self, central_bank, initial_cash=1000):
        super().__init__(central_bank, initial_cash)
        self.current_step = 0

    def get_state(self):
        l = len(self.central_bank.get_all_stock())
        
        owned_stocks = set(self.stocks_owned.keys())
        s = "".join(["0" if i in owned_stocks else "1" for i in range(l)])

        return int(s, 2)

        '''
        ABC
        000   - 0
        001   - 1  
        010   - 2
        011   - 3
        100   - 4
        101   - 5
        110   - 6
        111   - 7
        
        '''
        # A B _ F _
        # 1 0 0
        # 1 0 1
