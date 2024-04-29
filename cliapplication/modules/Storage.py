import json
from .Task import Task

class Storage: 
    tasks = [Task("lol","HEALTH", 2), Task("connard","HEALTH", 10)]
    def addTask(task):
        task.id = len(Storage.tasks)
        Storage.tasks.append(task)
    
    def deleteTask(task):
        Storage.tasks.remove(task)

    def persistTasks() -> None:
        jsonTask = json.dumps([task.__dict__ for task in Storage.tasks], default=lambda x: x.__dict__, indent=4)
        with open('tasks.json', 'w') as file:
            file.write(jsonTask)
    
    def fillStorage():
        """
            Need to be called once to populate the tasks with the data we already persisted
        """
        # Open a file in read mode ('r')
        with open('tasks.json', 'r') as file:
            # Read the entire contents of the file
            file_contents = file.read()
            Storage.tasks= json.loads(file_contents)
 



# Storage.persistTasks()
# Storage.fillStorage()
# print(Storage.tasks)


