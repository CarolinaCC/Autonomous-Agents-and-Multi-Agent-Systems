# ideias https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/stock-price/

class Event:
    def __init__(self, name, modifier):
        self.name = name
        self.modifier = modifier

    # returns True if the event applies to the stock, False otherwise
    def applies_to_stock(self, stock):
        pass

    # updates the value of the stock passed relating to the event.
    def update_stock(self, stock, current_step):
        if (self.applies_to_stock(stock)):
            stock.update_price(self.modifier * stock.price, current_step)

class NoneEvent:
    def applies_to_stock(self):
        return False

class ElonMuskPositiveTweetEvent(Event): #Uma companhia sobe bastante. Se calhar volta a descer rapidamente
    def __init__(self, name, modifier):
        super().__init__(name,modifier)
        #self.stocks_affected = Só quero que afecte uma stock, se calhar um one-hot array?
        #ou um nome de stock? Para isso preciso de ter lista dos nomes
        
        
class ElonMuskNegativeTweetEvent(Event): #Uma companhia desce bastante. Se calhar volta a subir rapidamente
    def __init__(self, name, modifier):
        super().__init__(name,modifier)
        #self.stocks_affected = Só quero que afecte uma stock, se calhar um one-hot array?
        #ou um nome de stock? Para isso preciso de ter lista dos nomes   
        
class GlobalPandemicEvent(Event): #Quase todas as companhias descem. Umas poucas sobem (farmacêuticas)
    def __init__(self, name, modifier):
        super().__init__(name,modifier)
        
class TechBreakthroughEvent(Event): #Uma companhia sobe e companhias rivais descem
    def __init__(self, name, modifier):
        super().__init__(name,modifier)
        
class WarrenBuffetListEvent(Event): #Warren Buffet invests in a list of stocks and they go up
    def __init__(self, name, modifier):
        super().__init__(name,modifier)
        
class IlegalMonopolyFineEvent(Event): #2+ companies are fined for having illegal monopoly (ou entao concorrencia desleal) and their shares drop somewhat


    
    