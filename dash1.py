import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Diosahestia1@localhost:3306/CatalogoTiendaVirtual')

query = "SELECT * FROM juegos;"
df = pd.read_sql(query, engine)



def create_figures():
    # Juegos más vendidos del 2020 en adelante según la calificación de usuarios
    fig1 = px.bar(df[df['Año'] >= 2020].nlargest(10, 'Cal. de usuarios'),
                  x='Titulo', y='Cal. de usuarios',
                  title='Top 10 Juegos más vendidos del 2020 en adelante según la calificación de usuarios')

    # Mejores videojuegos lanzados antes del 2020 según la calificación de usuarios y crítica
    fig2 = px.scatter(df[df['Año'] < 2020].nlargest(10, 'Cal. de usuarios'),
                      x='Cal. de usuarios', y='Cal. de critica', text='Titulo',
                      title='Top 10 Mejores videojuegos lanzados antes del 2020 según la calificación de usuarios y crítica')
    return fig1, fig2


def create_layout():
    fig1, fig2 = create_figures()
    return html.Div([
        html.H1("Análisis de Videojuegos"),

        #Juegos más vendidos del 2020 en adelante según la calificación de usuarios
        html.Div([
            html.H2("Juegos más vendidos del 2020 en adelante según la calificación de usuarios"),
            dcc.Graph(figure=fig1, id='graph1', style={'width': '80%', 'height': '400px'})
        ]),

        #Mejores videojuegos lanzados antes del 2020 según la calificación de usuarios y crítica
        html.Div([
            html.H2("Mejores videojuegos lanzados antes del 2020 según la calificación de usuarios y crítica"),
            dcc.Graph(figure=fig2, id='graph2', style={'width': '80%', 'height': '400px'})
        ]),


        dcc.Input(id='dummy-input', type='hidden', value='dummy')
    ])





