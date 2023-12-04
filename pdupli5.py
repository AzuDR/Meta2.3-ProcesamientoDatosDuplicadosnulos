""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 5. Realizar una función que reciba como parámetro un DataFrame y elimine los
renglones repetidos en el DataFrame Original. Debe retornar la cantidad de
renglones eliminados"""
import pandas as pd
data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
                    'rating': [4, 4, 3.5, 5.5, 5]})
#print(data)

def eliminar(data):
    dato1 = len(data)
    data.drop_duplicates(inplace=True)
    dato2 = len(data)
    res = (f"{data}\n\n\nLos renglones eliminados fueron: {dato1 - dato2}")
    return res
print(eliminar(data))
