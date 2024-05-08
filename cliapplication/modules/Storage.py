import json
import os
from ColorCli import Colors as Co
from Printer import Printer



class Storage:
    @classmethod
    def persist_tasks(cls) -> None:
        jsonTask = json.dumps(cls.profile_dict, indent=4)
         # task.json if tested from the module or ./modules/task.json if called from an external file
        with open('tasks.json', 'w') as file:
            file.write(jsonTask)
            
    @classmethod    
    def fillStorage(cls) -> bool:
        """
            Need to be called once to populate the tasks with the data we already persisted
        """
        
        # task.json if tested from the module or ./modules/task.json if called from an external file
        filepath = "tasks.json"
        
        print(os.path.isfile(filepath))
        if os.path.isfile(filepath):
            # print("is not working")
            with open('tasks.json', 'r') as file:
                # Read the entire contents of the file
                file_contents = file.read()
                tasks_data= json.loads(file_contents)
             # Convert each task dictionary back into a Task object
            cls.profile_dict = tasks_data
            Printer.print_system_message("Storage filled")
            return True
        else:
            Printer.print_debug_message("No tasks to fill")
            return False
        
    @classmethod
    def initializeProperty(cls) -> dict:
        
        filepath = "properties.json"
        
        # print(os.path.isfile(filepath))
        try:
            if os.path.isfile(filepath):
                # print("is working")
                
                tasks_data = None
                with open(filepath, 'r') as file:
                    # Read the entire contents of the file
                    file_contents = file.read()
                    tasks_data = json.loads(file_contents)
                # Convert each task dictionary back into a Task object
                cls.properties_storage = tasks_data
                cls.task_properties = cls.properties_storage["default"]
                Printer.print_debug_message(cls.properties_storage)
                Printer.print_debug_message(cls.task_properties)
                Printer.print_system_message(" ***storage filled*** ")
            else:
               
                cls.properties_storage = {
                    "default": {
                        "done": "bool",
                        "id": "str",
                        "content": "str",
                        "category": "str",
                    }
                }
                cls.task_properties = cls.properties_storage["default"]
                Printer.print_debug_message(cls.properties_storage)
                with open(filepath, 'w') as file:
                    file.write(json.dumps(cls.properties_storage, indent=4)) 
        except:
            Printer.print_error_message("Error in initializeProperty")
                   
    @classmethod    
    def persist_properties(cls) -> None:
        jsonTask = json.dumps(cls.properties_storage, indent=4)
        with open('properties.json', 'w') as file:
            file.write(jsonTask)
        
        



