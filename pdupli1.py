""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 1. Realizar una función que reciba como parámetro un DataFrame y retorne el
porcentaje de valores nulos de cada columna.
"""
import pandas as pd
import numpy as np

data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'cost(Dlls)': [np.nan, np.nan, np.nan, 48, 50],
                    'rating': [4, 4, 3.5, np.nan, 5]})
#print(data)
def valnull(data) :
    nullv= data.isnull().sum()
    pnulos = (nullv / len(data)) * 100
    return pnulos
print (valnull(data))