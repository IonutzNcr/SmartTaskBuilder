# from enum import Enum, auto

## my Categories
# class Category(Enum):
#     AMBITION = auto()
#     HEALTH =  auto()
#     MOTIVATION = auto()
#     DETERMINATION = auto()
#     CONCENTRATION = auto()
#     STATE_OF_MIND = auto()
#     PROBLEM_SOLVING = auto()
#     ADAPTABILITY = auto()
#     RESILIENCE = auto()
#     TIME_MANAGEMENT = auto()
#     COMMUNICATION_SKILLS = auto()
#     SELF_AWARENESS = auto()

from abc import ABC, abstractmethod
from typing import Type


class CategoryManagerInterface(ABC):
   
    @abstractmethod
    def add_category(name:str):
        """
        Add a Category to the dictionnary
        """
        pass
    
    @abstractmethod
    def delete_category(name:str):
        """
        Delete a Category from the dictionnary
        """
        pass
    
    @abstractmethod
    def update_category(name:str):
        """
        Update a Category from the dictionnary
        """
        pass

    
    @abstractmethod
    def list_items(category:str):
        """
        List all categories
        """
        pass
    
    @abstractmethod
    def list_categories():
        """
        List all categories
        """
        pass
    
class CategoryManager(CategoryManagerInterface):
    @classmethod
    def add_category(cls: Type['CategoryManager'],name:str):
        print("****** add category ******")
        if cls.profile_dict[cls.current_profile].get(name) is None:
            cls.profile_dict[cls.current_profile][name] = []
            cls.persist_tasks()
            print("add category")
        else:
            print("category already exists")
    @classmethod
    def delete_category(cls: Type['CategoryManager'], name:str):
        if cls.profile_dict[cls.current_profile].get(name) is not None:
            del cls.profile_dict[cls.current_profile][name]
            cls.persist_tasks()
            print("delete category")
        else:
            print("category does not exist")
    @classmethod
    def update_category(cls: Type['CategoryManager'], name:str, new_name:str):
        if cls.profile_dict[cls.current_profile].get(name) is not None:
            cls.profile_dict[cls.current_profile][new_name] = cls.profile_dict[cls.current_profile].pop(name)
            print("update category")
        else:
            print("category does not exist")
        
    @classmethod
    def list_items(cls: Type['CategoryManager'] ,category:str):
        print(cls.profile_dict[cls.current_profile][category])
        print("list items")
    @classmethod
    def list_categories(cls: Type['CategoryManager']):
        print(cls.profile_dict[cls.current_profile].keys())
        print("list categories")
# CategoryManager.add_category("ambition")
