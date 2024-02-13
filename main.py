from attributes.py import Attributes
from parameters.py import Parameters

def add_attribute():
    ...

def delete():
    ...

def display():
    ...

functions = {
    "add_attribute": add_attribute 
    "delete": delete
    "display": display 
}

def parse_user(command_line):
    return command_line

def main():
    inp = input("Enter a command:")
    command = parse_user(inp)

    functions[command]()

    return command == "exit"

while True():
    if main(): break
