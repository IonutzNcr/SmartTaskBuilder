from .Command import CommandsFunction
import re

class EventListener:
    @staticmethod
    def Listen(input_str: str):
        try:
            print("cool")
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
                getattr(CommandsFunction, action)(argument)
            else:
                getattr(CommandsFunction, action)()

        except Exception as e:
            print(e)

# Example usage:
# EventListener.Listen('add ')
