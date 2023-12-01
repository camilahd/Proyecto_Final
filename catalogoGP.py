import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import requests

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://gamepassport.net/")


data = {"Titulo": [], "Categoria": [], "Año": [], "Duracion": [],"Cal. de critica": [],"Cal. de usuarios": []}



soup = BeautifulSoup(navegador.page_source, "html.parser")
lista_divs = soup.find_all(name="div", attrs={"class": "d-flex flex-column me-2 mb-2 bg-dark rounded"})


for i in lista_divs:
    nombre = i.find('h6', attrs={"class": "lh-1"})
    data["Titulo"].append(nombre.text)
    cat = i.find('div', attrs={"class": "text-truncate"})
    data["Categoria"].append(cat.text)
    anno = i.find('span', attrs={"title":"Release year"})
    data["Año"].append(anno.text)
    duracion = i.find('span', attrs={"d-inline-flex align-items-center"})
    data["Duracion"].append(duracion.text)
    critica = i.find('div', attrs={"title": "Critic score"})
    data["Cal. de critica"].append(critica.text)
    publico = i.find('div', attrs={"title": "User score"})
    data["Cal. de usuarios"].append(publico.text)

data_df = pd.DataFrame(data)
data_df.to_csv("catalogoGP.csv")