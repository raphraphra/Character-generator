import random as rd

class attributes:
    
    def __init__(self, attribute, name):
        self.attribute = attribute
        self.length = len(attribute)
        self.name = name 
        
    def clear(self):
        self.attribute = []
        return self.attribute
    
    def add_attr(self, attribute):
        self.attribute.append(attribute)
        return self.attribute
    
    def pick(self):
        attr = rd.choice(self.attribute)
        return attr
   