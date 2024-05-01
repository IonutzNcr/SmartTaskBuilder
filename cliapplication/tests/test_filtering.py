import unittest

class FilterManager:
    @classmethod
    def filter(cls, profile_dic, filter: str) -> None:
        print("filtering for: " + filter)
        filter_dict = {}
        category = filter.split(":")[0]
        
        _filter = filter.split(":")[1]
        # print("category: " + category)
        # print("filter: " + _filter)
        #TODO: for categories which is appart for the task attributes
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
      

profile_dic = {
    "hobby": [
        {
            "done": False,
            "id": "1",
            "content": "content1",
            "type": "category1"
        },
        {
            "done": False,
            "id": "2",
            "content": "content2",
            "type": "category1"
        }
    ],
    "programmation": [
        {
            "done": False,
            "id": "3",
            "content": "content3",
            "type": "category2"
        },
        {
            "done": False,
            "id": "4",
            "content": "content4",
            "type": "category1"
        }
    ]
}

#TODO: category:hobby diff from type:category1

class TestFilterManager(unittest.TestCase):
    def test_filter(self):
        expected = {
            "programmation": [
        {
            "done": False,
            "id": "3",
            "content": "content3",
            "type": "category2"
        },
        {
            "done": False,
            "id": "4",
            "content": "content4",
            "type": "category1"
        }
            ]
        }
        filter_dict = FilterManager.filter(profile_dic, "category:programmation")
        self.assertEqual(filter_dict, expected , msg="filtering by category:programmation expected to return {}".format(expected))
        
    def test_filter_attribute(self):
        expected = {
            "hobby": [
                {
                    "done": False,
                    "id": "1",
                    "content": "content1",
                    "type": "category1"
                },
                {
                    "done": False,
                    "id": "2",
                    "content": "content2",
                    "type": "category1"
                }
            ],
            "programmation": [
                    {
                        "done": False,
                        "id": "4",
                        "content": "content4",
                        "type": "category1"
                    }
            ]
        }
        filter_dict = FilterManager.filter(profile_dic, "type:category1")
        self.assertEqual(filter_dict, expected , msg="filtering by type:category1 expected to return {}".format(expected))



__name__ == "__main__" and unittest.main()