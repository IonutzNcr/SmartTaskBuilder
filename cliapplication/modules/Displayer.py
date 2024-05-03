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
        _profile_dic = profile_dic
        task_properties = task_prop
        print(task_properties)
        print("**inside displayTable**")
        # print(profile_dic) # there is no pb in the profile_dic
        # print(task_properties) # there is no pb in the task_properties

        str_header = ""
        dic_strsize = {"done": 5}

        try:
            for property in task_properties:
                print(property)
                if property != "done":
                    dic_strsize[property] = len(property)
            print(dic_strsize)
        except Exception as e:
            print(e)
            raise ValueError("TESTError in displayTable")
            
        try:
            for category in _profile_dic:
                
                # print("category is: ")
                # print(category)
                for task in _profile_dic[category]:
                    # print(task)
                    for property in task:
                    
                        if property != "done":
                            if property not in dic_strsize:
                                dic_strsize[property] = len(property)
                            if len(str(task[property])) > dic_strsize.get(property,0):
                                dic_strsize[property] = len(str(task[property]))
        except Exception as e:
            print(e)
            raise ValueError("Error in displayTable")
        # print( dic_strsize)
        try:
            for property in task_properties:
                print(Colors.WARNING + property + Colors.ENDC)
                print(dic_strsize[property])
                str_header += property + (" "*(dic_strsize[property] - len(property))) + " | "
            # print(str_header)            
            print(Colors.BOLD + str_header + Colors.ENDC)
            print("-"*(sum(dic_strsize.values()) + (5*3)))
        except Exception as e:
            print(e)
            raise ValueError("TestError in displayTable")
         
        body_table = ""
        str_row = ""
        for category in _profile_dic:
            for task in _profile_dic[category]:
                for property in task_properties:
                    if property == "done":
                        if task[property]:
                            if searchMode:
                                str_row +="[ x ]" + " | "
                            else:
                                str_row += Colors.OKGREEN + "[ x ]" + " | "
                        else:
                            str_row += "[   ]" + " | "
                    if property != "done" and property in task: 
                        str_row += str(task[property]) + (" " * (dic_strsize[property] - len(str(task[property])))) + " | "
                    
                    if property != "done" and property not in task:
                        str_row += " " * dic_strsize[property] + " | "
                        # print (" "*dic_strsize[property] + " | ")
                        # break # to avoid the error
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