""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 4. Realizar una función que reciba como parámetro un DataFrame, una lista con los
nombres de las columnas a verificar y una cadena. La cadena solo puede ser mean,
bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los valores nulos
por el método especificado y retornar el DataFrame modificado."""
import pandas as pd
import numpy as np
data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'cost(Dlls)': [55, 57, np.nan, np.nan, 50],
                    'rating': [4, 4, 3.5, np.nan, 5]})
#print(data)

columnas = ["cost(Dlls)","rating"]

while True:
    cadena = input("Escribe el metodo a utilizar: mean, bfill, ffill")
    if cadena == "mean" or cadena == "bfill" or cadena == "ffill":
        break
    else:
        print("La cadena debe ser 'mean', 'bfill' o 'ffill'")
def sustval(data, columnas, cadena):
    for col in data[columnas]:
        prom = data[col].mean().round(2)
        if cadena == "mean":
            data[col].fillna(prom, inplace=True)
        elif cadena == "bfill":
            data.bfill(inplace=True)
        elif cadena == "ffill":
            data.ffill(inplace=True)
    return data
print(sustval(data, columnas, cadena))
