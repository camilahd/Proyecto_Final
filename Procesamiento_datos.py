import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Data frame
data = pd.read_csv("catalogoGP.csv", index_col=0)

#Observar que tipo de datos tiene nuestro data frame y ejemplos
print(data.dtypes)
print(data.sample(5))

#Modificar la columna Duracion, quitarle la h
data["Duracion"] = data['Duracion'].str.replace('h', '')
data["Duracion"] = data['Duracion'].str.replace('— ', '')

#Remplazar algunos caracteres para identificar los valores nulos
data.replace('tbd', np.nan, inplace=True)
data.replace('?', np.nan, inplace=True)
data.replace('TBA', np.nan, inplace=True)
print(data.isnull())
#print(data["Cal. de critica"].isnull().sum())

#Asignar los tipos de datos
data["Año"] = pd.to_numeric(data["Año"])
data["Duracion"] = pd.to_numeric(data["Duracion"])
data["Cal. de critica"] = pd.to_numeric(data["Cal. de critica"])
data["Cal. de usuarios"] = pd.to_numeric(data["Cal. de usuarios"])

#Comprobacion
print(data.dtypes)
print(data.sample(5))
print(data.sample(5))
#Cargar datos en un archivo
data.to_csv("procesado.csv")

#Observar valores atipicos
sns.boxplot(x=data['Año']) #del 2007 hacia atras son valores fuera de rango
plt.show()

sns.boxplot(x=data['Duracion']) # duracion mayor a 42.5 es fuera de rango, especialmente arriba de 100
plt.show()

sns.boxplot(x=data['Cal. de critica']) #los que estan debajo de 56 estan fuera del rango
plt.show()

sns.boxplot(x=data['Cal. de usuarios']) #los que estan por debajo de 3.3 estan fuera de rango
plt.show()
