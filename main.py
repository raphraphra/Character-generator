from attributes.py import Attributes
from parameters.py import Parameters

def create_attribute(name, [content]):
    name = Attributes(name)
    name.add_attr([content])

def add_content(name, [content]):
    name.add_attr([content])

def remove_content(name, [content]):
    
    
