"""
Lunch the program
"""

from modules.EventListener import EventListener

class Runner :
    def run():
        print("Welcome to my wonderfull cli app! Tape help to get some help :)")
        isRunning = True
       
        while isRunning:
            
            input_us = input("What do you want to do:\n--> ")
            if input_us == "exit":
                isRunning = False
                break 
            EventListener.Listen(input_us)
       
# App.run()