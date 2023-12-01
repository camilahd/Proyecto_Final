import pandas as pd
from catalogoGP import archivo
from Procesamiento_datos import limpieza
from CatalogoProcesado import redondear
from duplicadosProyecto import depuracion

data = archivo()
data = pd.DataFrame(data)
data = limpieza(data)
data = redondear(data)
data = depuracion(data)

data.to_csv("Catalogo_Terminado.csv")
