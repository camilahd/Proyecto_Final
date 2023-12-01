import pandas as pd
from Procesamiento_datos import limpieza
from CatalogoProcesado import redondear

data = pd.read_csv("catalogoGP.csv", index_col=0)
data = pd.DataFrame(data)
data = limpieza(data)
data = redondear(data)
