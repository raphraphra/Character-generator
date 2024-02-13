from attributes.py import Parameters

class Container:
    
    def __init__(self, param = []): 
        self.content = param
     
        
    def add_param(self, param):
        for att in self.content:
            if att.name == str(param):  
                self.content.remove(att)
        self.content.append(param)
        return self.content
        
    def remove_attribute(self, param):
        cond = input("Remove an element or an entire parameter? E/P")
        if cond == "E": 
            for index, att in enumerate(self.content):
                if att.name == param:
                    attrib = input("Which attribute to remove?")
                    att.clear_attribute(attrib)
                    
            return "Your demand was invalid"
            
        if cond == "P":
            for index, att in enumerate(self.param):
                if att.name == param:
                    self.content.pop(index)
                    return self.param
            return f"{param} not found in parameters."
                  
    # Will interact better with python's builtin stuff
    def __str__(self):
        res = [f"Your character's {att.name} is {att.pick()}" for att in self.content]
        return "\n".join(res)
    
