from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

dash_app = Dash(__name__)



dash_app.layout = html.Div([
    html.H4('Interactive color selection with simple Dash example'),
    html.P("Select color:"),
    dcc.Dropdown(
        id="dropdown",
        options=['Gold', 'MediumTurquoise', 'LightGreen'],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@dash_app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], # replace with your own data source
                    marker_color=color))
    return fig

app = FastAPI()
app.mount("/", WSGIMiddleware(dash_app.server))
#app.run(debug=False)