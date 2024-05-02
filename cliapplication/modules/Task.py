from abc import ABC, abstractmethod

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
    task_properties = {
        "done": bool,
        "id": str,
        "content": str,
        "category": str,
    }

    @classmethod
    def add_property(cls, name: str) -> None:
        cls.task_properties[name] = str

    @classmethod
    def add_task(cls, task: dict) -> None:
        try:
            cls.profile_dict[cls.current_profile][task["category"]].append(task)
            cls.persist_tasks()
            # print(cls.profile_dict)
            print("add Task")
        except:
            raise Exception("Error in add_task")
            
    @classmethod
    def check_task(cls, id: str) -> None:
        for category in cls.profile_dict[cls.current_profile]:
            for task in cls.profile_dict[cls.current_profile][category]:
                if task["id"] == id:
                    task["done"] = True
                    cls.persist_tasks()
                    print("checked task")
                    return
        print("checked task")
    @classmethod
    def delete_task(cls, id: str) -> None:
        for category in cls.profile_dict[cls.current_profile]:
            for task in cls.profile_dict[cls.current_profile][category]:
                if task["id"] == id:
                    cls.profile_dict[cls.current_profile][category].remove(task)
                    cls.persist_tasks()
                    print(f"Task with ID {id} deleted from {category}")
                    return
        
        print("delete task")
    def generate_tasks(input: str) -> None:
        print(f"generated taks depending on {input}")
    
# TaskManager.addTask("je veux mourrir")