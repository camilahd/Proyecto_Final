import dash
import dash_bootstrap_components as dbc
import dash1 as d1
import dash2 as d2
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN], suppress_callback_exceptions=True)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Tienda Virtual", className="display-4"),
        html.Hr(),
        html.P(
            " Analisis de los datos", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Dashboard 1", href="/dash1", active="exact"),
                dbc.NavLink("Dashboard 2", href="/dash2", active="exact"),
                dbc.NavLink("GitHub", href="https://www.github.com",
                            target="_blank", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("A continuacion se muestran las graficas de barras y tabla con la informacion recabada: ")
    elif pathname == "/dash1":
        return d1.create_layout()
    elif pathname == "/dash2":
        return d2.create_layout_2()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run(debug=True)
    #app.run_server(port=8888)