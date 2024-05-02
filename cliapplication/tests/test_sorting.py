import unittest
import re

class SortingManager:
    @staticmethod
    def sort(profile_dic, category):
        sorted_dict = {}
        for _category in profile_dic:
            sorted_dict[_category] = sorted(profile_dic[_category], key=lambda x: x[category])
        return sorted_dict
    
class ConversionManager:
    @staticmethod
    def convert_to_number(type):
        """
        Convert a string to a number if possible
        return the number if possible or False
        """
        try:
            float(type)
            return float(type)
        except ValueError:
            try:
                nb = re.sub(r'[^\d.]', '', type)
                print(nb)
                return float(nb)
            except ValueError:
                return False

        

class TestSortingManager(unittest.TestCase):
    def test_convert_to_number(self):
        self.assertEqual(ConversionManager.convert_to_number("1"),1.0)
        self.assertEqual(ConversionManager.convert_to_number("1.0"), 1.0)
        self.assertFalse(ConversionManager.convert_to_number("a"))
        self.assertFalse(ConversionManager.convert_to_number("a.0"))
        self.assertEqual(ConversionManager.convert_to_number("1a"),1.0)
        self.assertEqual(ConversionManager.convert_to_number("100.2xp"),100.2)

    def test_sort(self):
        profile_dic = {
            "hobby": [
                {
                    "done": False,
                    "id": "1",
                    "content": "haha",
                    "type": "category1"
                },
                {
                    "done": False,
                    "id": "3",
                    "content": "aaa",
                    "type": "category1"
                }
            ],
            "programmation": [
                {
                    "done": False,
                    "id": "2",
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
        expected = {
            "hobby": [
                {
                    "done": False,
                    "id": "1",
                    "content": "haha",
                    "type": "category1"
                },
                {
                    "done": False,
                    "id": "4",
                    "content": "aaa",
                    "type": "category1"
                }
            ],
            "programmation": [
                {
                    "done": False,
                    "id": "2",
                    "content": "content4",
                    "type": "category1"
                },
                {
                    "done": False,
                    "id": "3",
                    "content": "content3",
                    "type": "category2"
                }
            ]
        }
        self.assertEqual(SortingManager.sort(profile_dic, "id"), expected)
        self.assertEqual(SortingManager.sort(profile_dic, "type"), expected)
        self.assertEqual(SortingManager.sort(profile_dic, "content"), expected)
        self.assertEqual(SortingManager.sort(profile_dic, "done"), expected)