import json
import os
from ColorCli import Colors as Co



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
        # print("wtf")
        # print(cls)
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
            print(Co.WARNING +" ***storage filled*** "+ Co.ENDC)
            return True
        else:
            print("im here wtf")
            return False
        
 
# Storage.persistTasks()
# Storage.fillStorage()
# print(Storage.tasks)


