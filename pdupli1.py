""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 1. Realizar una función que reciba como parámetro un DataFrame y retorne el
porcentaje de valores nulos de cada columna.
"""
import pandas as pd
df = "boston_house_prices.csv"
data = pd.read_csv(df)
#print(data)
def valnull(data) :
    nullv= data.isnull().sum()
    pnulos = (nullv / len(data)) * 100
    return pnulos
print (valnull(data))