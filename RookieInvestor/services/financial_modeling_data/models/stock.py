class Stock:
    def __init__(self, payload):
        self.stock = payload
    
    @property
    def name(self):
        return self.stock['name']
        