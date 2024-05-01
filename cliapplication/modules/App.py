"""
Lunch the program
"""

from EventListener import EventListener
from Profile import ProfileManager

class Runner :
    def run():
        ProfileManager.init_profile()
        print("Welcome to my wonderfull cli app! Tape help to get some help :)")
        isRunning = True
       
        while isRunning:
            
            input_us = input("What do you want to do:\n--> ")
            
            if input_us == "exit":
                isRunning = False
                break 
            EventListener.Listen(input_us)
       
Runner.run()