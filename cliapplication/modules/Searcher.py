from abc import ABC, abstractmethod
from Profile import ProfileManager
from Displayer import Displayer
from ColorCli import Colors
import re

class SearcherManagerInterface(ABC):
    @abstractmethod
    def search(input:str) -> None:
        pass

class Searcher(SearcherManagerInterface, ProfileManager):
    @classmethod
    def search(cls, input:str) -> None:
        print("searching for: " + input)
        search_dict = {}
        try:
            for category in cls.profile_dict[cls.current_profile]:
                print("category: " + category)
                for task in cls.profile_dict[cls.current_profile][category]:
                    #TODO: im here 
                    for attr in task:
                        print("attr: " + attr)
                        if attr == "done":
                            continue
                        if input in task[attr]:
                            # print("input found"+ str(input))
                            # print("search_dict", search_dict.get(category))
                            if search_dict.get(category) is None:
                                search_dict[category] = []
                            if task not in search_dict[category]:
                                search_dict[category].append(task)
        except:
            raise ValueError("Error in search")
        Displayer.displayTable(search_dict, cls.task_properties, searchMode = True, searchKey = input)
        print("searched")