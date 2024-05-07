import unittest
import json
import os



class Storage:
    
    properties_storage = None
    task_properties = None
    
    @classmethod
    def initializeProperty(cls) -> dict:
        
        filepath = "properties.json"
        
        # print(os.path.isfile(filepath))
        try:
            if os.path.isfile(filepath):
                print("is working")
                
                tasks_data = None
                with open(filepath, 'r') as file:
                    # Read the entire contents of the file
                    file_contents = file.read()
                    tasks_data = json.loads(file_contents)
                # Convert each task dictionary back into a Task object
                cls.properties_storage = tasks_data
                cls.task_properties = cls.properties_storage["default"]
                print(cls.properties_storage)
                print(cls.task_properties)
                print(" ***storage filled*** ")
            else:
               
                cls.properties_storage = {
                    "default": {
                        "id": "str",
                        "category": "str",
                        "task": "str",
                        "done": "bool"
                    }
                }
                cls.task_properties = cls.properties_storage["default"]
                print(cls.properties_storage)
                with open(filepath, 'w') as file:
                    print("propertiesprint")
                    print(cls.properties_storage)
                    print(json.dumps(cls.properties_storage))
                    file.write(json.dumps(cls.properties_storage, indent=4)) 
        except:
            print("Error in initializeProperty")


class TestInitiTask(unittest.TestCase):
    def test_init_task(self):
        expected = { 
                "id": "str",
                "category": "str",
                "task": "str",
                "done": "bool"  
                }
        Storage.initializeProperty()
        self.assertEqual(Storage.task_properties, expected)
        
    def test_init_task2(self):
        """
        Test pour vérifier si le fichier properties.json existe et si la function inittask gere bien ce cas la
        """
        expected = { 
                "id": "str",
                "category": "str",
                "task": "str",
                "done": "bool"  
                }
        Storage.initializeProperty()
        self.assertEqual(Storage.task_properties, expected)