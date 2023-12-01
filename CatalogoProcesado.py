import pandas as pd
df = pd.read_csv("CatalogoP.csv", index_col=0)
data = pd.DataFrame(df)

def redondear(data):
    data['Duracion'] = data['Duracion'].round(2)
    data['Cal. de critica'] = data['Cal. de critica'].round(2)
    data['Cal. de usuarios'] = data['Cal. de usuarios'].round(2)
    data.to_csv("CatalogoProcesado.csv")