from ColorCli import Colors
from OpenAi import Assisstant
from Profile import ProfileManager
from Searcher import Searcher
from Displayer import Displayer
from Filter import Filter
from Sorter import SorterManager
from Printer import Printer
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
        Printer.print_debug_message("step 1")
        task_by_openai = Assisstant.assignCategory(input_us)
        task_by_openai["id"] = str(uuid.uuid4())
        task_by_openai["done"] = False
        Printer.print_debug_message(task_by_openai)
        Printer.print_debug_message("im here in add method")
        ProfileManager.add_task(task_by_openai)
        Printer.print_system_message("Task added successfully")


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
            Printer.print_error_message("Task not found")
    
    def delete(id):
            found_task = False
            for category in ProfileManager.profile_dict[ProfileManager.current_profile]:
                for task in ProfileManager.profile_dict[ProfileManager.current_profile][category]:
                    if task['id'] == id:
                        ProfileManager.delete_task(id)
                        found_task = True
                        break
            
            if found_task == False:
                Printer.print_error_message("Task not found")   
                
    def use(name:str):
        ProfileManager.change_profile(name)
        Printer.print_system_message("profile changed to " + name)
    
    #TODO: ADD DYNAMIC ATTRIBUTES // is done I think.
    def add_property(name:str):
        ProfileManager.add_property(name)
        
    
    def category(name:str):
        ProfileManager.add_category(name)
        

    def all_categories():
        Printer.print_debug_message(ProfileManager.profile_dict[ProfileManager.current_profile].keys())

    def delete_category(name:str):
        ProfileManager.delete_category(name)
        

    def search(input:str):
        Searcher.search(input)

    def filter(input:str):
        filtered_dict = Filter.filter(ProfileManager.profile_dict[ProfileManager.current_profile],input)
        # print(filtered_dict)
        Displayer.displayTable(filtered_dict, ProfileManager.task_properties)
        
    def sort(input:str):
        try:
            dt = SorterManager.convert_to_array(ProfileManager.profile_dict[ProfileManager.current_profile])
            # Printer.print_debug_message(dt)
            data = SorterManager.sorting(dt, input)
            # Printer.print_debug_message(data)
            Displayer.displayTableWithSorting(data)
        except ValueError as e:
            Printer.print_error_message("Error in sort method | Comand.py L101 ", e)
            
    def generate(_input:str):
        """
        Generate tasks with the input
        """
        tasks = Assisstant.assign_tasks(_input)
        for category in tasks:
            for task in tasks[category]:
                task["id"] = str(uuid.uuid4())
                task["done"] = False
        Displayer.displayTable(tasks, ProfileManager.task_properties)
        
        try:
            resp = input("Do you want to save the tasks? y/n")
            if resp == "y":
                for category in tasks:
                    
                    if ProfileManager.profile_dict[ProfileManager.current_profile].get(category) is None:
                        ProfileManager.profile_dict[ProfileManager.current_profile][category] = []
                    for task in tasks[category]:
                        ProfileManager.add_task(task)
                Printer.print_system_message("Tasks saved")
            else:
                Printer.print_system_message("Tasks not saved")
        except:
            Printer.print_error_message("Error in generate method | Command.py L127")
        
       
       