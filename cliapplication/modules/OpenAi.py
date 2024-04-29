from openai import OpenAI
from dotenv import load_dotenv
import os
import json


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
        completion = Assisstant.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You have to give one of these categories : HEALTH, PROBLEM_SOLVING or MOTIVATION,  to my task as well as an explanation to why is that and not the other categories as well as an exp points dependending on the difficulty, all in a json objet containing this propery:category, explanation , experience, and difficulty   "},
                {"role":"user", "content": input }
            ]
        )
        return json.loads(completion.choices[0].message.content)




print (Assisstant.assignCategory("SE NOURRIR"))



