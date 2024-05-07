from Command import CommandsFunction
from Command import ProfileManager
from Printer import Printer
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
                Printer.Message.print_error_message("Invalid number of arguments. Please check the command with help command.")
            
            # Call the appropriate function from CommandsFunction class
            if argument is not None:
                try:
                    getattr(CommandsFunction, action)(argument)
                except Exception as e:
                    Printer.print_error_message("Invalid command (L43 | EventListener.py)")
            else:
                try:  
                    getattr(CommandsFunction, action)()
                except Exception as e:
                    Printer.print_error_message("Invalid command (L47 | EventListener.py)")
                         
        except Exception as e:
            
            # Printer.print_debug_message(e)
            Printer.Message.print_error_message("Error in EventListener.py L53", e)
