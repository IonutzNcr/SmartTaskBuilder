from ColorCli import Colors
from OpenAi import Assisstant
from Profile import ProfileManager
from Searcher import Searcher
from Displayer import Displayer
from Filter import Filter
import json
import uuid

class CommandsFunction:
    """
    store the functions to be executed in function of the input
    """
    
    def help():
        print("View: too see all the todos\nAdd to add a todo\nCheck make a task done")
    
    def add(input_us:str):
        # get the category from openai; add with the storage, persist
        task_by_openai = Assisstant.assignCategory(input_us)
        task_by_openai["id"] = str(uuid.uuid4())
        task_by_openai["done"] = False
        
        ProfileManager.add_task(task_by_openai)
        # print(task_by_openai)
        print(" added " + input_us)


    #TODO Refactoring the view function
    def view():
        profile_dic = ProfileManager.profile_dict[ProfileManager.current_profile]
        task_properties = ProfileManager.task_properties
        Displayer.displayTable(profile_dic, task_properties)
    def check(id:str):
        # print(Colors.OKBLUE +"starting checking ..." + Colors.ENDC)
        found_task = False
        for category in ProfileManager.profile_dict[ProfileManager.current_profile]:
            for task in ProfileManager.profile_dict[ProfileManager.current_profile][category]:
                if task['id'] == id:
                    task['done'] = True
                    ProfileManager.persist_tasks()
                    # print(Colors.OKGREEN + "Task has been checked successfully." + Colors.ENDC)
                    # print(ProfileManager.profile_dict[ProfileManager.current_profile])
                    found_task = True
                    break
        
        if found_task == False:
            raise Exception("not id found")
    
    def delete(id):
            found_task = False
            for category in ProfileManager.profile_dict[ProfileManager.current_profile]:
                for task in ProfileManager.profile_dict[ProfileManager.current_profile][category]:
                    if task['id'] == id:
                        ProfileManager.delete_task(id)
                        found_task = True
                        break
            
            if found_task == False:
                raise Exception("not id found")        
    def use(name:str):
        ProfileManager.change_profile(name)
        print("profile changed to " + name)
    
    def category(name:str):
        ProfileManager.add_category(name)
        print("category added")

    def all_categories():
        print(ProfileManager.profile_dict[ProfileManager.current_profile].keys())

    def delete_category(name:str):
        ProfileManager.delete_category(name)
        print("category deleted")

    def search(input:str):
        Searcher.search(input)

    def filter(input:str):
        filtered_dict = Filter.filter(ProfileManager.profile_dict[ProfileManager.current_profile],input)
        # print(filtered_dict)
        Displayer.displayTable(filtered_dict, ProfileManager.task_properties)