import re
import pandas as pd
# from Displayer import Displayer

class SorterManager:
    @classmethod
    def convert_to_number(cls, value):
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
    #TODO: make it dynamique for any category
    @classmethod
    def convert_to_array(cls, dictionary):
        """
        Convert my dictionnary to a an array of dictionnary   
        """
        try:
            # print(dictionary)
            
            
            df = pd.DataFrame()
            for category in dictionary:
                print(category)
                df_category = pd.json_normalize(dictionary[category])
                df = pd.concat([df, df_category], ignore_index=True) 
            
           

            # Ajout d'une colonne pour identifier la catégorie
            #no need of this rite
            # df_hobby['category'] = 'hobby'
            # df_other['category'] = 'other'

          
            
            print("***end***")
            return df
        except:
            #wrong message description
            raise ValueError("The dictionary must have the format: {category: [{},{},{}]}")
        
        
    #TODO: implement the convertion of number string to number ex 20xp -> 20
    @classmethod
    def sorting(cls, dataframe, input):
        """
        Dataframe must be sorted and having this format:
        [{},{},{}]
        """
        print("*******displaying sorted table step 2")
        try:
            name = input.split(":")[0]
            order = input.split(":")[1]
            print(name + " " + order)
            if order.upper() != 'ASC' and order.upper() != 'DESC':
                raise ValueError("Order must be ASC or DESC")  
        except:
            raise ValueError("Argument of sort must be in the format: param:asc or param:desc")
        _order = False
        if order.upper() == 'ASC':
            _order = True
        elif order.upper() == 'DESC':
            _order = False
        else: 
            raise ValueError("Order must be ASC or DESC")
        df = dataframe.sort_values(by=name, ascending=_order, ignore_index=True)
        # print(df.to_dict(orient='records'))
        return df.to_dict(orient='records')
    
    
# test = {
#     "hobby": [
#         {
#             "done": False,
#             "id": "1",
#             "content": "content1",
#             "type": "category1",
#             "exp": "20xp",
#         },
#         {
#             "done": False,
#             "id": "2",
#             "content": "content2",
#             "type": "category1",
#             "exp": "10xp",
#         }
#     ],
#     "programmation": [
#         {
#             "done": False,
#             "id": "4",
#             "content": "content4",
#             "type": "category1",
#             "exp": "12xp",
#         }
#     ]
# }

# data = SorterManager.sorting(SorterManager.convert_to_array(test), 'category', 'DESC')
# Displayer.displayTableWithSorting(data)