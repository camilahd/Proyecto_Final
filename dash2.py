import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output,callback
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Diosahestia1@localhost:3306/CatalogoTiendaVirtual')

query = "SELECT * FROM juegos;"
df = pd.read_sql(query, engine)

def update_graph_and_table():
    category_ratings = df.groupby('Categoria').agg({'Cal. de usuarios': 'mean', 'Cal. de critica': 'mean'}).reset_index()
    fig = px.bar(category_ratings, x='Categoria', y=['Cal. de usuarios', 'Cal. de critica'],
                 title='Categoría mejor puntuada según la calificación de usuarios y crítica')
    table_data = category_ratings.to_dict('records')
    return fig, table_data

@callback(
    [Output('graph', 'figure'),
     Output('table', 'data')],
    [Input('dummy-input', 'value')]
)
def update_data(dummy_input):
    fig, table_data = update_graph_and_table()
    return fig, table_data


def create_layout_2():
    return html.Div([
        html.H1("Análisis de Videojuegos 2"),

        # Categoria mejor puntuada
        html.Div([
            html.H2("Categoría mejor puntuada según la calificación de usuarios y crítica"),
            dcc.Graph(id='graph'),
            dash_table.DataTable(
                id='table',
                columns=[
                    {'name': col, 'id': col} for col in ['Categoria', 'Cal. de usuarios', 'Cal. de critica']
                ],
                style_table={'height': '200px', 'overflowY': 'auto'},
            ),
        ]),

        dcc.Input(id='dummy-input', type='hidden', value='dummy')
    ])