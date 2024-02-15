from parameters.py import Parameters
from container.py import Container
import sys

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
        print(str(container), end = "\n")
        seeds.append(str(container))

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
        inp = input().split(" ")
        if inp == "display":
            print(functions.get(inp[0], skip)(*inp[1:]))
            continue
    
        functions.get(inp[0], skip)(*inp[1:])
        
    return 
