from attributes.py import Attributes

class Parameters:
    
    def __init__(self, param = []): 
        self.param = param
     
        
    def add_param(self, param):
        for att in self.param:
            if att.name == str(param):  
                self.param.remove(param)
        self.param.append(param)
        return self.param
        
    def remove_attr(self, param):
        cond = input("Remove an element or an entire parameter? E/P")
        if cond == "E": 
            for index, att in enumerate(self.param):
                if att.name == param:
                    attrib = input("Which attribute to remove?")
                    if attrib not in att.attribute:
                        return f"{attrib} not found in {att}"
                    att.attribute.remove(attrib)
                    return att.attribute
            return "Your demand was invalid"
            
        if cond == "P":
            for index, att in enumerate(self.param):
                if att.name == param:
                    self.param.pop(index)
                    return self.param
            return f"{param} not found in parameters."
                  
    # Will interact better with python's builtin stuff
    def __str__(self):
        res = [f"Your character's {att.name} is {att.pick()}" for att in self.param]
        return "\n".join(res)

