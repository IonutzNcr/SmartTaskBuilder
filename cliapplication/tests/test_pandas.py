import pandas as pd
import unittest

class SortingPandas():
    def sorting(self):
        data = {
                "hobby": [
                    {
                        "done": False,
                        "id": "1",
                        "content": "content1",
                        "type": "category1",
                        "exp": "20xp",
                    },
                    {
                        "done": False,
                        "id": "2",
                        "content": "content2",
                        "type": "category1",
                        "exp": "10xp",
                    }
                ],
                "programmation": [
                   
                    {
                        "done": False,
                        "id": "4",
                        "content": "content4",
                        "type": "category1",
                        "exp": "12xp",
                    }
                ]
            }

        # Normalisation et création de DataFrames individuels
        df_hobby = pd.json_normalize(data['hobby'])
        df_programmation = pd.json_normalize(data['programmation'])

        # Ajout d'une colonne pour identifier la catégorie
        df_hobby['category'] = 'hobby'
        df_programmation['category'] = 'programmation'

        # Concaténation des deux DataFrames en un seul
        df = pd.concat([df_hobby, df_programmation], ignore_index=True)
        df = df.sort_values(by='exp', ascending=False, ignore_index=True)
        print(df.to_dict(orient='records'))
        return df.to_dict(orient='records')
        # print(df.iloc[0].tolist())
    
    
class TestSortingPandas(unittest.TestCase):
    def test_sorting(self):
        sorting = SortingPandas()
        expected = [{
            "done": False,
            "id": "1",
            "content": "content1",
            "type": "category1",
            "exp": "20xp",
        },
       
       {
            "done": False,
            "id": "2",
            "content": "content2",
            "type": "category1",
            "exp": "10xp",
        },
        {
            "done": False,
            "id": "4",
            "content": "content4",
            "type": "category1",
            "exp": "12xp",
        },]
        self.assertEqual(sorting.sorting(), expected)