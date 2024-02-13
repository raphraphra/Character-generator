from attributes.py import Attributes
from parameters.py import Parameters

def main() -> bool:
    print("Hello. Let's a build a character !")
    state_machine = "addAttribute"
    parameters = Parameters()
    
    match(state_machine):
            
        case "addAttribute":
                
            check = input("Build a new attribute? Yes or No.")
                
            while check == "Yes":
                              
                new_param = input("What attribute do you want to create?")
                new_param = Attributes(str(new_param))
                add = ""

                while add != "/":

                    add = input(f"Add an element into {new_param} (/ to escape).")

                    new_param.add_attr(add)

                check = input("Build another attribute?")

    

        case "Delete":
            check = "Yes"
            while check == "Yes":
                attr = input("Which attribute to delete from?")
                parameters.remove_attr(attr)

                check = input("Continue deleting?")


        case "Display":
            roll = "Yes"
            while roll == "Yes":
                parameters.__str__()
                roll = input("Roll another time?")



        case "Escape"
    
            return False

        state_machine = input("What do you want to do?")


while True:


    


