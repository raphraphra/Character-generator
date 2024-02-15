from parameters.py import Parameters
from container.py import Container
import sys



class Parameters:
    
    def __init__(self, name, attribute = []):
        self.content = attribute
        self.name = name 
        
    def clear_attribute(self,attribute):
        self.content.remove(attribute)
        return self.content
        
   
    def add_attr(self, attribute):
        for i in attribute:
            if i in self.content:
                self.content.remove(i)
            self.content.append(i)
        return self.content
    
    def pick(self):
        return rd.choice(self.content)
        
       
    
class Container:
    
    def __init__(self, param = []): 
        self.content = param
     
        
    def add_param(self, param):
        for att in self.content:
            if att.name == str(param):  
                self.content.remove(att)
        self.content.append(param)
        
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
    
    


    
    
dic = {}
container = Container()
seeds = []

    
def create_parameter(*args):
    dic[args[0]] = Parameters(args[0], [])
    return  dic[args[0]].content

def add_attribute(*args):
    dic[args[0]].add_attr(args[1:])
    return dic[args[0]].content

def clear_attribute(*args):
    dic[args[0]].clear_attribute(args[1:])
    return dic[args[0]].content

def add_parameter(*args):
    container.add_param(dic[args[0]])
    
def display(*args):
    for i in range(int(args[0])):
        print(str(container))
        seeds.append(str(container))
    
def parse_lign(string):
    return string.split(" ")

def stop():
    print(seeds)
    sys.exit()

def show_commands():
    for i in functions.keys():
        print(f"{i} \n")

def show_param():
    for i in dic.keys():
        print(f"{i} \n")
        
def skip(*args):
    print("Invalid Command")
    pass

def show_seeds(*args):
    for i, j in enumerate(seeds):   
        print(f"Seed {i} : {j} \n")

functions = {
    "c_param" : create_parameter,
    "add_att": add_attribute,
    "clear": clear_attribute,
    "add_param": add_parameter,
    "display" : display,
    "stop": stop,
    "show_commands" : show_commands,
    "show_seeds" : show_seeds,
    "show_param" : show_param
}
    
    
def main():
    while True:
        inp = ""
        inp = parse_lign(input())
        if inp == "display":
            print(functions.get(inp[0], skip)(*inp[1:]))
            continue
    
        functions.get(inp[0], skip)(*inp[1:])
        
    return 
