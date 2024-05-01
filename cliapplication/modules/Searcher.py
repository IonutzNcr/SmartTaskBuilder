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
        for category in cls.profile_dict[cls.current_profile]:
            print("category: " + category)
            for task in cls.profile_dict[cls.current_profile][category]:
                #TODO: im here 
                for attr in task:
                    if attr == "done":
                        continue
                    if input in task[attr]:
                        print("input found"+ input)
                        new_input = re.sub(input, Colors.BG_YELLOW + input + Colors.ENDC, task[attr])
                        print("new input: " + new_input)
                        task[attr] = new_input
                        print("search_dict", search_dict.get(category))
                        if search_dict.get(category) is None:
                            search_dict[category] = []
                        if task not in search_dict[category]:
                            search_dict[category].append(task)
        Displayer.displayTable(search_dict, cls.task_properties)
        print("searched")