#ELIMINACION DE DUPLICADOS Y LLENADO DE DATOS

#IMPORTAMOS LIBRERIAS
import pandas as pd
import numpy as np

#IMPORTAMOS EL ARCHIVO DEL PROYECTO
df = pd.read_csv("datasets/procesado.csv", index_col=0)
data = pd.DataFrame(df)
#print(data.sample(5))

"""data = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
                    'cost(Dlls)': [55, 55, np.nan, 48, 50],
                    'rating': [4, 4, 3.5, np.nan, 5]})"""
# VERIFICAMOS SI TIENE DATOS DUPLICADOS,EN CASO DE QUE TENGA SE VAN A ELIMINAR
def valdup(data):
    dupli = data.duplicated().sum()
    if dupli == 0:
        print("El dataset no tiene valores duplicados")
    else:
        data.drop_duplicates(inplace=True)
    return data

# CHECAMOS EL RESULTADO
# print(valdup(data))
valdup(data)


columnas = ["Duracion","Cal. de critica","Cal. de usuarios"]
while True:
    cadena = input("Escoge el metodo para rellenar valores faltantes:")
    if cadena == "mean" or cadena == "bfill" or cadena == "ffill":
        break
    else:
        print("La cadena debe ser 'mean', 'bfill' o 'ffill'")

def sustval(data, columnas, cadena):
    prom = data[columnas].mean().round(2)
    if cadena == "mean":
        data.fillna(prom,inplace=True)
    elif cadena == "bfill":
        data.bfill(inplace=True)
    elif cadena == "ffill":
        data.ffill(inplace=True)
    return data
# CHECAMOS EL RESULTADO
# print(sustval(data, columnas, cadena))
sustval(data, columnas, cadena)


# Cargar datos en un archivo
data.to_csv("CatalogoP.csv")
