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
from Printer import Printer


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
            Printer.print_system_message("Category: " + name + " added")
        else:
            Printer.print_error_message("Category already exists")
            
    @classmethod
    def delete_category(cls: Type['CategoryManager'], name:str):
        if cls.profile_dict[cls.current_profile].get(name) is not None:
            del cls.profile_dict[cls.current_profile][name]
            cls.persist_tasks()
            Printer.print_system_message("Category: " + name + " deleted")
        else:
            Printer.print_error_message("Category does not exist")
            
    @classmethod
    def update_category(cls: Type['CategoryManager'], name:str, new_name:str):
        if cls.profile_dict[cls.current_profile].get(name) is not None:
            cls.profile_dict[cls.current_profile][new_name] = cls.profile_dict[cls.current_profile].pop(name)
            Printer.print_system_message("Category: " + name + " updated to " + new_name)
        else:
            Printer.print_error_message("Category does not exist")
        
    @classmethod
    def list_items(cls: Type['CategoryManager'], category:str):
        Printer.print_debug_message(cls.profile_dict[cls.current_profile][category])
        
        
    @classmethod
    def list_categories(cls: Type['CategoryManager']):
        Printer.print_debug_message(cls.profile_dict[cls.current_profile].keys())

