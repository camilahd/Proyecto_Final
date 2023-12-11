#PROFESOR ESTAS SON LAS LIBERIAS QUE DEBE DE TENER PARA QUE SE EJECUTE CORRECTAMENTE
import pandas as pd #version 2.1.4
import numpy as np #version 1.26.2
import seaborn as sns #version 0.13.0
import matplotlib.pyplot as plt #version 3.8.2


from catalogoGP import archivo
from Procesamiento_datos import limpieza
from CatalogoProcesado import redondear
from duplicadosProyecto import depuracion
from sqlalchemy import create_engine
import CONSTANTES as cs

data = archivo()
data = pd.DataFrame(data)
data = limpieza(data)
data = redondear(data)
data = depuracion(data) #escoja el metodo bfill o ffill para rellenar los datos faltantes

data.to_csv("Catalogo_Terminado.csv")
#print(data.dtypes)

#CONEXION MYSQL

cadena_conexion = f"mysql+mysqlconnector://{cs.USER}:{cs.PASSWORD}@{cs.SERVER}/{cs.NAME_BD}"
#print(cadena_conexion)
engine = create_engine(cadena_conexion)
conexion = engine.connect()
#print(conexion)
datosdata = pd.read_csv("Catalogo_Terminado.csv", index_col=0)
datosdata.to_sql("juegos", conexion, if_exists="append", index=False)
print("Se hara la siguiente consulta para asegurar que se hizo la conexion:\n\n")
query = "Select * from juegos where Año= 2017 "
resultados = pd.read_sql(query, conexion)
print(resultados)
print("La primera parte del proyecto ha TERMINADO")

#PARA CORRER EL MENU ESTAS SON LAS LIBREBRIAS
import dash
import dash_bootstrap_components as dbc
import dash1 as d1
import dash2 as d2
from dash import Input, Output, dcc, html

#LIBRERIAS DEL DASHBOARD 1
