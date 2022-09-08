import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import sklearn
import joblib 
from dash import dash_table
from dash.exceptions import PreventUpdate

app = Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])


df = pd.DataFrame({
    "Temperature": [],
    "Relative Humidity": [],
    "Absolute Humidity": [],
    "Sensor 1": [],
    "Sensor 2": [],
    "Sensor 3": [],
    "Sensor 4": [],
    "Sensor 5": [],
    "target_carbon_monoxide": [],
    "target_benzene": [],
    "target_nitrogen oxides": []
})
    


app.layout = html.Div([
    dbc.Row([
        dbc.Col([
        dbc.Card([
            html.Div(["WEATHER PREDICTION APP"], className="heading"),
            html.Br(),
            dbc.Row([
                html.Div(["Atmospheric Conditions"]),
                html.Br(),
                dbc.Row([
                    dbc.Col(["Temperature(C)"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-temp", type= 'number', placeholder=f"temperature")
                    ] + [html.Div(id="out-temp")])
                ]),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Relative Humidity"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-rel-hum", type= 'number', placeholder=f"relative humidity")
                    ] + [html.Div(id="out-rel-hum")])
                    ]),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Absolute Humidity"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-abs-hum", type= 'number', placeholder=f"absolute humidity")
                    ] + [html.Div(id="out-abs-hum")])
                ])
            ],
                    justify="evenly"),
            html.Br(),
            dbc.Row([
                html.Div(["Sensor Data"]),
                html.Br(),
                dbc.Row([
                    dbc.Col(['Sensor 1']),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-sens-1", type= 'number', placeholder=f"sensor 1")
                    ] + [html.Div(id="out-sens-1")], className = 'sensor-inputs')
                ],  ),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Sensor 2"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-sens-2", type= 'number', placeholder=f"sensor 2")
                    ] + [html.Div(id="out-sens-2")], className = 'sensor-inputs')
                    ],  ),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Sensor 3"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-sens-3", type= 'number', placeholder=f"sensor 3")
                    ] + [html.Div(id="out-sens-3")], className = 'sensor-inputs')
                ], ),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Sensor 4"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-sens-4", type= 'number', placeholder=f"sensor 4")
                    ] + [html.Div(id="out-sens-4")], className = 'sensor-inputs')
                ], ),
                html.Hr(style= {'color': 'white'}),
                dbc.Row([
                    dbc.Col(["Sensor 5"]),
                    dbc.Col([
                        dcc.Input(
                        id=f"input-sens-5", type= 'number', placeholder=f"sensor 5")
                    ] + [html.Div(id="out-sens-5")], className = 'sensor-inputs')
                ], className = 'sensor-cols')
            ], justify = "evenly"),
            html.Hr(style= {'color': 'white'}),
            dbc.Row([
                dbc.Button(
            "Process", id="data-processor", className="process-button", n_clicks=0
        ),
        html.Span(id="data-process", style={"verticalAlign": "middle"}),
            ], justify = 'evenly')
        ],
                 className="app-card")
    ], width = 5)
        , 
        dbc.Col([
            
            dash_table.DataTable(
                id='table-container',
                data=[],
                columns=[{"name":i,"id":i,'type':'text'} for i in df.columns],
                style_table={'overflow':'scroll','height':600},
                style_cell={'textAlign':'center'},
                row_deletable=True,
                editable=True)
        ], width= 7)
    ],
             className="div-space")
])

@app.callback(
    Output("table-container", "data"), 
    [Input("data-processor", "n_clicks")],
    [State('table-container', 'data'),
    State('table-container', 'columns')],
    [State('input-temp', "value")],
    [State('input-rel-hum', "value")],
    [State('input-abs-hum', "value")],
    [State("input-sens-1", "value")],
    [State("input-sens-2", "value")],
    [State("input-sens-3", "value")],
    [State("input-sens-4", "value")],
    [State("input-sens-5", "value")],
    )
def add_row(n_clicks, rows, columns, temp, rel_hum,abs_hum, sens1, sens2, sens3, sens4, sens5):
    X = [temp, rel_hum,abs_hum, sens1, sens2, sens3, sens4, sens5]
    data = []
    if n_clicks is None:
        raise PreventUpdate
    y = model.predict(data)
    y = y.reshape(-1, 1)
    data.extend(iter(y))
    rows.append({c['id']: r for c,r in zip(columns, data)})
    return rows



# table data collection
# @app.callback(
#     [Output("table-container", "data"), Output("table-container", "columns")],
#     [Input("data-processor", "n_clicks")]
# )

# @app.callback(
#     Output("example-output", "children"),
#     [Input("example-button", "n_clicks")],
# )
def model():
    return


if __name__ == '__main__':
    model = joblib.load("predModel.pkl")
    app.run_server(debug=True)