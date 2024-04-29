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

        # print("done | id | content | category | exp \n" + ("-" * 60))
        str_notstr = ""
        dic_strsize = {"done":5,"id":0,"content":0, "category":0, "xp":0}
        for task in tasks:
            for size in dic_strsize:
                if size != "done":
                    if len(str(getattr(task,size))) > dic_strsize[size]:
                        dic_strsize[size] = len(str(getattr(task,size))) 
                
        str_notstr =  "done" + (" "*(dic_strsize["done"] - len("done"))) + " | " + "id" + (" "*(dic_strsize["id"] - len("id"))) + " | " + "content" + (" "*(dic_strsize["content"] - len("content"))) + " | " + "category" + (" "*(dic_strsize["category"] - len("category")))+ " | " + "xp" + (" "*(dic_strsize["xp"] - len("xp")))
        print(Colors.BOLD + str_notstr + Colors.ENDC)
        print("-"*(dic_strsize["done"] + dic_strsize["id"] + dic_strsize["content"] + dic_strsize["category"]+ dic_strsize["xp"] + (4*3)))
        for task in tasks:
            if task.done:
                print(Colors.OKGREEN + "[ x ]"+ (" "*(dic_strsize["done"] - len("[ x ]"))) +  " | " + str(task.id) + (" "*(dic_strsize["id"] - len(str(task.id))))  + " | " + task.content + (" "*(dic_strsize["content"] - len(task.content)))  + " | " + task.category + (" "*(dic_strsize["category"] - len(task.category)))  + " | " + str(task.xp) + (" "*(dic_strsize["xp"] - len(str(task.xp))))  + Colors.ENDC)
                print("-"*(dic_strsize["done"] + dic_strsize["id"] + dic_strsize["content"] + dic_strsize["category"]+ dic_strsize["xp"] + (4*3)))
            else:
                print("[   ]"+ (" "*(dic_strsize["done"] - len("[   ]"))) +  " | " + str(task.id) + (" "*(dic_strsize["id"] - len(str(task.id))))  + " | " + task.content + (" "*(dic_strsize["content"] - len(task.content)))  + " | " + task.category + (" "*(dic_strsize["category"] - len(task.category)))  + " | " + str(task.xp) + (" "*(dic_strsize["xp"] - len(str(task.xp)))))
                print("-"*(dic_strsize["done"] + dic_strsize["id"] + dic_strsize["content"] + dic_strsize["category"]+ dic_strsize["xp"] + (4*3)))

    def check(id):
        found_task = False
        for task in Storage.tasks:
            if task.id == task.id:
                task.done = True
                Storage.persistTasks()
                found_task = True
                break
        
        if found_task == False:
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
            
        
    