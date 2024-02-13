import random as rd


class Parameters:
    
    def __init__(self, name, attribute = []):
        self.content = attribute
        self.name = name 
        
    def clear_attribute(self,attribute):
        self.content.remove(attribute)
        
   
    def add_attr(self, attribute):
        for i in attribute:
            if i in self.content:
                self.content.remove(i)
            self.content.append(i)
    
    def pick(self):
        return rd.choice(self.content)
