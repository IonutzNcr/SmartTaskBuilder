"""
Lunch the program
"""

from modules.EventListener import EventListener
from modules.Storage import Storage

class Runner :
    def run():
        Storage.fillStorage()
        print("Welcome to my wonderfull cli app! Tape help to get some help :)")
        isRunning = True
       
        while isRunning:
            
            input_us = input("What do you want to do:\n--> ")
            
            if input_us == "exit":
                isRunning = False
                break 
            EventListener.Listen(input_us)
       
# App.run()