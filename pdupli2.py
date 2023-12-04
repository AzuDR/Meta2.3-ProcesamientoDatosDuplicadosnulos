""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 2. Realizar una función que reciba como parámetro un DataFrame y retorne el número
de renglones duplicados.
"""
import pandas as pd
data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
                    'rating': [4, 4, 3.5, 15, 5]})
#print(data)
def valdup(data):
    dupli = data.duplicated().sum()
    return dupli
print(valdup(data))