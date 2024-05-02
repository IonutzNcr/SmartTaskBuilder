from Command import CommandsFunction
from Command import ProfileManager
import re

#TODO: Better Implementation required for better ux 
class EventListener:
    @staticmethod
    def Listen(input_str: str):
        try:
            # print("****Listener working...")
            action = None
            argument = None
            
            # Regular expression pattern to match arguments in quotes
            pattern = r'(["\'])(.*?)\1'
            matches = re.findall(pattern, input_str)
            
            # Extracting the arguments from matches
            if matches:
                argument = matches[0][1]  # Extract the argument from the first match
            
            # Split input string by space to get the action
            input_arr = input_str.split()
            
            # Check the number of arguments
            if len(input_arr) == 2 and argument is None:
                action = input_arr[0]
                argument = input_arr[1]
            elif len(input_arr) == 1 and argument is None:
                action = input_arr[0]
            elif argument is not None:
                action = input_arr[0]
            else:
                raise Exception("Too many arguments or nothing has been written")
            
            # Call the appropriate function from CommandsFunction class
            if argument is not None:
                try:
                    getattr(CommandsFunction, action)(argument)
                except Exception as e:
                    print(e)
                    print("In Argument condition Event Listener")
            else:
                try:  
                    getattr(CommandsFunction, action)()
                except Exception as e:
                    print(e)
                    print(action)
                    print("In No Argument condition Event Listener")
        except Exception as e:
            print("In Event Listener")
            print(e)
            print("end")

# Example usage:
# ProfileManager.init_profile()
# # EventListener.Listen("add 'faire les courses'")
# # EventListener.Listen("add 'mettre le linge à sécher'")
# EventListener.Listen('view')
# EventListener.Listen('check "713c7193-0345-4286-a30a-7baf64374eaf"')
# EventListener.Listen('delete "96d0a3fa-800a-4631-b560-e791e6d094ad"')
# EventListener.Listen('view')
