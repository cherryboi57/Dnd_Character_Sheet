class Passive_Trait:
    def __init__(self, n, source):
        self.name = n
        self.source = source.name
        self.description = None
        source.passive_traits[n] = self
    
    def info(self):
        print(self.name + " (" + self.source + "):")
        print(self.description)