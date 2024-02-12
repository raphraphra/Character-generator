import random as rd

class attributes:
    
    def __init__(self, attribute, name):
        self.attribute = attribute
        self.name = name 
        
    def clear(self):
        self.attribute = []
    
    def add_attr(self, attribute):
        self.attribute.append(attribute)
    
    def pick(self):
        return rd.choice(self.attribute)
   