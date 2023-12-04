""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 3. Realizar una función que reciba como parámetro un DataFrame y un máximo
porcentaje. Este debe eliminar todas las columnas que superen o igualen el máximo
porcentaje de valores nulos establecidos en el DataFrame Original. Retornar la lista
nombres de columnas eliminadas. Validar que el porcentaje máximo esté entre 0 y 1."""
import pandas as pd
import numpy as np
data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'cost(Dlls)': [np.nan, np.nan, np.nan, 48, 50],
                    'rating': [4, 4, 3.5, np.nan, 5]})
#print(data)

while True:
    perc = float(input("Introduce el maximo porcentaje. (Debe de ser entre 1 y 0)"))
    if perc > 0 and perc < 1:
        break
    else:
        print("El porcentaje maximo debe de estar entre 0 y 1")

def maxper(data, perc):
    coleliminar = []
    for col in data.columns:
        pcnulos = data[col].isnull().sum() / len(data)
        if pcnulos >= perc:
            coleliminar.append(col)
    ndata = data.drop(columns=coleliminar)
    return f"Las columnas eliminadas fueron: {coleliminar}\n\n{ndata}"
#PARA PROBAR EL POGRAMA SE USO EL PORCENTAJE MAXIMO DE 0.5
print(maxper(data, perc))
