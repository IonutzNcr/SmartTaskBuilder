from .Storage import Storage
from .ColorCli import Colors
from .OpenAi import Assisstant
from .Task import Task
import json
import uuid

class CommandsFunction:
    """
    store the functions to be executed in function of the input
    """
    
    def help():
        print("View or -V: too see all the todos\nAdd or -A to see add a todo\nCheck or -c to make a task done")
    
    def add(input_us:str):
        # get the category from openai; add with the storage, persist
        task_by_openai = Assisstant.assignCategory(input_us)
        
        
        Storage.addTask(Task(content=input_us, category = task_by_openai['category'], xp=task_by_openai['experience'], id=str(uuid.uuid4())))
        Storage.persistTasks()
        # print(task_by_openai)
        print(" added" + input_us)


    #TODO working on the display of the todo table in the cli
    def view():
        tasks =  Storage.tasks

        print("done | id | content | category | exp \n" + ("-" * 60))
        for task in tasks:
            if task.done:
                print(Colors.OKGREEN + "[ x ] " + "| " +str(task.id) +" | " + task.content + " | " + task.category+ " | " + str(task.xp) +"\n" +  "-----"+ ("-" *len(task.content)) + Colors.ENDC)
            else:
                print("[   ] " + "| " +str(task.id) +" | " + task.content + " | " + task.category+ " | " + str(task.xp) +"\n" +   "-----"+ ("-" *len(task.content)))
            
    def check(id):
        if Storage.tasks[int(id)]:
            Storage.tasks[int(id)].done = True
            Storage.persistTasks()
        else: 
            raise Exception("not id found")
    
    def delete(id):
        # Find the task by id
        task_to_delete = None
        for task in Storage.tasks:
            if task.id == task.id:
                task_to_delete = task
                break

        if task_to_delete is not None:
            resp = input("Are you sure? (y/n): ")
            if resp not in ["y", "n"]:
                raise Exception("Not a valid command")
            elif resp == "y":
                Storage.tasks.remove(task_to_delete)
                Storage.persistTasks()
                print(Colors.WARNING + "Task has been deleted successfully." + Colors.ENDC)
            else:
                print("Nothing has changed.")
        else:
            raise Exception("No task found with ID: {}".format(task.id))
            
        
    