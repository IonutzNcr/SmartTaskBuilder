

class Filter:
    #TODO: make it work for done:True special case
    @classmethod
    def filter(cls, profile_dic, filter: str) -> None:
        print("filtering for: " + filter)
        filter_dict = {}
        print(filter)
        category = filter.split(":")[0]  
        _filter = filter.split(":")[1]
        print("category: " + category)
        print("filter: " + _filter)
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