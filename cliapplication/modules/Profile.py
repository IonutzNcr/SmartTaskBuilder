from abc import ABC, abstractmethod
from Category import CategoryManager
from Storage import Storage
from Task import TaskManager


class ProfileManagerInterface(ABC):
    @property
    @abstractmethod
    def current_profile():
        """
        A string referring to the current profile
        """
        pass
    @property
    @abstractmethod
    def profile_dict():
        """
        A dictionnary which contains all useful information
        about profiles, categories and tasks
        """
        pass
    
    @abstractmethod
    def init_profile(cls):
        """
        Initialize the Profile, if no profile are saved in the store,
        will preconfigure a basic Profile containing 3 categories: "hobby", "work", "other"
        """
        pass
    
    @abstractmethod
    def add_profile(name:str):
        """
        Add a Profile to the dictionnary with no categories and no tasks
        """
        pass
    
    @abstractmethod
    def delete_profile(name:str):
        """
        Delete a Profile from the dictionnary
        """
        pass
    
    @abstractmethod
    def change_profile(name:str):
        """
        Change the current profile, if the profile does not exist, will create a profile with the name
        """
        pass
    
    @abstractmethod
    def persist_profiles():
        """
        Persist the profiles in the store
        """
        pass


class ProfileManager(ProfileManagerInterface, CategoryManager, TaskManager, Storage):
    current_profile = "default"
    profile_dict = {}

    @classmethod
    def init_profile(cls):
        cls.current_profile = "default"
        if cls.fillStorage():
            print("profile filled")
        else :
            cls.profile_dict = {cls.current_profile: {"hobby": [], "work": [], "other": []}}            
        print("profile initialized")
        cls.persist_tasks()
    

    #TODO : implement the following methods
    @classmethod
    def add_profile(name:str):
        """
        Not gonna implement it because u can use change_profile instead
        """
        print("profile added")
    @classmethod
    def delete_profile(cls, name:str):
        response = input("Are you sure you want to delete this profile ?\n By deleting this profile everything that comes with will be deleted forever\n (y/n)")
        if response == "y":
            del cls.profile_dict[name]
            cls.persist_profiles()
            print("profile deleted")
        else:
            print("profile not deleted")
    @classmethod
    def change_profile(cls, name:str):
        if cls.profile_dict.get(name) is not None:
            cls.current_profile = name
        else:
            cls.profile_dict[name] = {}
            cls.current_profile = name
            cls.persist_profiles()
        print("profile changed")
    @classmethod
    def persist_profiles(cls):
        cls.persist_tasks()
        print("profiles persisted")
    
