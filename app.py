import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        dbc.Card([
            html.Div(["WEATHER PREDICTION APP"]),
            dbc.Row([
                dbc.Col([])
                ])
        ], className = "app-card")
    ], className="div-space")
])

if __name__ == '__main__':
   app.run_server(debug=True)