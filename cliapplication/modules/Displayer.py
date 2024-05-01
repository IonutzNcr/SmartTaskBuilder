from abc import ABC, abstractmethod
from ColorCli import Colors

class DisplayerManagerInterface(ABC):
    @abstractmethod
    def displayTable(cls, data) -> None:
        pass

class Displayer(DisplayerManagerInterface):
    @classmethod
    def displayTable(cls, profile_dic, task_prop) -> None:
        print("*******displaying table")
        profile_dic = profile_dic
        task_properties = task_prop

        str_header = ""
        dic_strsize = {"done": 5}
        for category in profile_dic:
            # print("category is: ")
            # print(category)
            for task in profile_dic[category]:
                # print(task)
                for property in task:
                   
                    if property != "done":
                        if property not in dic_strsize:
                            dic_strsize[property] = len(property)
                        if len(str(task[property])) > dic_strsize.get(property,0):
                            dic_strsize[property] = len(str(task[property]))
        for property in task_properties:
          
            str_header += property + (" "*(dic_strsize[property] - len(property))) + " | "
        print(Colors.BOLD + str_header + Colors.ENDC)
        print("-"*(sum(dic_strsize.values()) + (5*3)))
       
        str_row = ""
        for category in profile_dic:
            for task in profile_dic[category]:
                for property in task_properties:
                    if property == "done":
                        if task[property]:
                            str_row += Colors.OKGREEN + "[ x ]" + Colors.ENDC + " | "
                        else:
                            str_row += "[   ]" + " | "
                    if property != "done":
                        str_row += str(task[property]) + (" "*(dic_strsize[property] - len(str(task[property])))) + " | "
                print(str_row)
                print("-"*(sum(dic_strsize.values()) + (5*3))) # compter les | de facon dynamique
                str_row = ""