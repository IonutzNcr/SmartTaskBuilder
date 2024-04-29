import json
import os
from .Task import Task


class Storage: 
    tasks = []
    
    def addTask(task):
        Storage.tasks.append(task)
    
    def deleteTask(task):
        Storage.tasks.remove(task)

    def persistTasks() -> None:
        jsonTask = json.dumps([task.__dict__ for task in Storage.tasks], default=lambda x: x.__dict__, indent=4)
        with open('./modules/tasks.json', 'w') as file:
            file.write(jsonTask)
    
    def fillStorage():
        """
            Need to be called once to populate the tasks with the data we already persisted
        """
        # print("doooooo")
        filepath = "./modules/tasks.json"
        # print("Current Working Directory: ", os.getcwd())
        print(os.path.isfile(filepath))
        if os.path.isfile(filepath):
            # print("is not working")
            with open('./modules/tasks.json', 'r') as file:
                # Read the entire contents of the file
                file_contents = file.read()
                tasks_data= json.loads(file_contents)
             # Convert each task dictionary back into a Task object
            for task_data in tasks_data:
                task = Task(task_data['content'], task_data['category'], task_data['xp'], task_data['id'], task_data['done'])
                Storage.tasks.append(task)

        else:
            # print("im here wtf")
            Storage.tasks = []
        
 



# Storage.persistTasks()
# Storage.fillStorage()
# print(Storage.tasks)


