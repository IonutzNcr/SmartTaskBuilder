from openai import OpenAI
from dotenv import load_dotenv
from Profile import ProfileManager
import os
import json
from Printer import Printer


# Print all environment variables
# for key in os.environ:
#     print(key, "=", os.environ[key])

class Config:
    def initialize ():
        load_dotenv()


class Assisstant:

    Config.initialize()
   
    client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])
    def assignCategory(input):
        categories = ProfileManager.profile_dict[ProfileManager.current_profile].keys()
        if len(categories) == 0:
            raise Exception("You have to create a category first!")
        try:
            properties = ProfileManager.task_properties
            categories_str = " ".join([category for category in categories])
            properties_str = " ".join([property for property in properties])
            completion = Assisstant.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"system", "content":"You have to give one of these categories :" +  categories_str + "and return a dictionnary in python with the following properties: " + properties_str },
                    {"role":"user", "content": input},
                ]
            )
            return json.loads(completion.choices[0].message.content)
        except:
            Printer.print_error_message("Error in the onepai response")
    
    @classmethod
    def assign_tasks(cls, input):
        categories = ProfileManager.profile_dict[ProfileManager.current_profile].keys()
        if len(categories) == 0:
            raise Exception("You have to create a category first!")
        properties = ProfileManager.task_properties
        categories_str = " ".join([category for category in categories])
        properties_str = " ".join([property for property in properties])
        completion = Assisstant.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You are now a manager so you have to creates tasks depending on the user which is your boss.You have to give one of these categories :" +  categories_str + "and return a list of dictionnary in python with the following properties: " + properties_str + " Here is an example of what is expected: {'hobby':[{'id':2323,'content':'Jouer','category':'hobby'}],'sport':[{'id':23232, 'content':'10 minutes of playing','category':'sport' }] } in a json format" },
                {"role":"user", "content": input},
            ]
        )
        try:
            # print (completion.choices[0].message.content)
            return json.loads(completion.choices[0].message.content)
        except:
            raise Exception("Error in the onepai response")


# print (Assisstant.assignCategory("SE NOURRIR"))



