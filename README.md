# Character-generator

## Concept

This tiny project was inspired by another one by a friend of mine. The concept was simple - a character generator based on parameters entered by the user. However, he added a tkinter interface to simplify navigation. 
My idea is the name, but it uses a command terminal instead (something similar, at least.)

## Classes

Okay. Though I wanted to use OOP as training, it might not be the best idea. 
Two classes :
Parameters that contain attributes (for instance, Name -> "Louis", "Adam")
Container : contains the parameters.
Many customs methods were added, though they're not actually required. Using the default List class would've done the trick too. But well. 

## Terminal

Using a simple parser, you enter the command's name then its relevant arguments. It's all pretty intuitive hopefully. 
Example : c_param Name will create a parameter named "Name".
          add_att Name Louis Adam will, well, add the strings Louis and Adam to said parameter, in this case Name. 

Other useful commands include show_commands, show_seeds, and show_param.
At the end of it all, you can use the command "display" to generate a character with random attributes. These seeds are then stored in a variable for your liking. 

Table of all comands:

|Commands|Action|Argument|
|--------|------|--------|
|c_param |Creates a new parameter|Name|
|add_att |Adds attributes to a parameter|Name, contents|
|clear|Remove a certain attribute from a parameter, or an entire parameter|Name (attribute is later asked)|
|add_param|Adds a parameter to the container|Parameter|
|display|Generates a seed|None|
|stop|Exits the code|None|
|show_commands|Displays all of the commands|None|
|show_seeds|Displays all seeds in order|None|
|show_param|Displays all current parameters|None|

