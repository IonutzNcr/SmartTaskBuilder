from ColorCli import Colors
from Printer import Printer

class Filter:
    #TODO: make it work for done:True special case
    @classmethod
    def filter(cls, profile_dic, filter: str) -> None:
        filter_dict = {}
        Printer.Message.print_system_message("Filtering for: " + filter)
        category = filter.split(":")[0]  
        _filter = filter.split(":")[1]
       
        if category == "category":
            filter_dict[_filter] = profile_dic[_filter]
        else:
            for _category in profile_dic:
               
                for task in profile_dic[_category]:
                    if task[category] == _filter:   
                        if filter_dict.get(_category) is None:
                            filter_dict[_category] = []
                        filter_dict[_category].append(task)
                       

        return filter_dict