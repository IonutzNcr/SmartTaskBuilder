from abc import ABC, abstractmethod
from Printer import Printer



class TaskManagerInterface(ABC):
    @property
    @abstractmethod
    def task_properties() -> dict:
        pass

    @abstractmethod
    def add_property(cls, name: str):
        pass
    @abstractmethod
    def add_task(cls,task: dict) -> None:
        """
        Add a Task to the dictionnary
        """
        pass
    @abstractmethod
    def check_task(id:str)-> None:
        pass
    @abstractmethod
    def delete_task(id:str)-> None:
        pass
    @abstractmethod
    def generate_tasks(input:str) -> None:
        pass

class TaskManager(TaskManagerInterface):
    #has to be initialized
    properties_storage = None; #has to be a dict
    task_properties = None; # has to be a dict

    @classmethod
    def init(cls) -> None:
        storage = cls.initializeProperty()
        cls.properties_storage = storage
        cls.task_properties = storage[cls.current_profile]
        Printer.print_system_message("init TaskManager")
        
    @classmethod
    def add_property(cls, name: str) -> None:
        try:
            cls.task_properties[name] = "str"
            #TODO: call the functions that persist the properties
            cls.persist_properties()
        except:
            raise Exception("Error in add_property")
    
    def del_property(cls, name:str) -> None:
        del cls.task_properties[name]

    @classmethod
    def add_task(cls, task: dict) -> None:
        try:
            cls.profile_dict[cls.current_profile][task["category"]].append(task)
            cls.persist_tasks()
            
        except:
            raise Exception("Error in add_task")
            
    @classmethod
    def check_task(cls, id: str) -> None:
        for category in cls.profile_dict[cls.current_profile]:
            for task in cls.profile_dict[cls.current_profile][category]:
                if task["id"] == id:
                    task["done"] = True
                    cls.persist_tasks()
                    Printer.print_system_message("Task has been checked successfully.")
                    return
        print("checked task")
        
    @classmethod
    def delete_task(cls, id: str) -> None:
        for category in cls.profile_dict[cls.current_profile]:
            for task in cls.profile_dict[cls.current_profile][category]:
                if task["id"] == id:
                    cls.profile_dict[cls.current_profile][category].remove(task)
                    cls.persist_tasks()
                    Printer.print_system_message(f"Task with ID {id} deleted from {category}")
                    return
        Printer.print_error_message("Task not found")
    #not implemented / not used  
    def generate_tasks(input: str) -> None:
        Printer.print_system_message(f"generated taks depending on {input}")
    
# TaskManager.addTask("je veux mourrir")