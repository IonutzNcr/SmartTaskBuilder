from abc import ABC, abstractmethod
from ColorCli import Colors
import re
class DisplayerManagerInterface(ABC):
    @abstractmethod
    def displayTable(cls, data) -> None:
        pass

class Displayer(DisplayerManagerInterface):
    @classmethod
    def displayTable(cls, profile_dic, task_prop, searchMode = False, searchKey = None) -> None:
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
         
        body_table = ""
        str_row = ""
        for category in profile_dic:
            for task in profile_dic[category]:
                for property in task_properties:
                    if property == "done":
                        if task[property]:
                            if searchMode:
                                str_row +="[ x ]" + " | "
                            else:
                                str_row += Colors.OKGREEN + "[ x ]" + " | "
                        else:
                            str_row += "[   ]" + " | "
                    if property != "done": 
                        str_row += str(task[property]) + (" " * (dic_strsize[property] - len(str(task[property])))) + " | "
                body_table += str_row + Colors.ENDC + "\n"
                body_table += ("-"*(sum(dic_strsize.values()) + (5*3))) +"\n" # compter les | de facon dynamique
                str_row = ""
        
        if searchMode:
            body_table_searched = re.sub(r'('+re.escape(searchKey)+')', Colors.BG_YELLOW + r'\1' + Colors.ENDC, body_table)
            print (body_table_searched)
        else:
            print(body_table)
        
        
    @classmethod
    def displayTableWithSorting(cls, dataframe):
        """
        Dataframe must be sorted and having this format:
        [{},{},{}]
        """
        print("*******displaying sorted table")
        dic_strsize = {"done": 5}
        if len(dataframe) == 0:
            raise ValueError("Dataframe is empty")
            return {}
        else:
            for task in dataframe:
                for property in task:
                    if property != "done":
                        if property not in dic_strsize:
                            dic_strsize[property] = len(property)
                        if len(str(task[property])) > dic_strsize.get(property,0):
                            dic_strsize[property] = len(str(task[property]))
            str_header = ""
            for property in task:
                str_header += property + (" "*(dic_strsize[property] - len(property))) + " | "
                
            print(Colors.BOLD + str_header + Colors.ENDC)
            print("-"*(sum(dic_strsize.values()) + (5*3)))
            
            for task in dataframe:
                str_row = ""
                for property in task:
                    if property == "done":
                        if task[property]:
                            str_row += Colors.OKGREEN + "[ x ]" + " | "
                        else:
                            str_row += "[   ]" + " | "
                    if property != "done":
                        str_row += str(task[property]) + (" "*(dic_strsize[property] - len(str(task[property]))) + " | ")
                print(str_row + Colors.ENDC)
                print("-"*(sum(dic_strsize.values()) + (5*3)))