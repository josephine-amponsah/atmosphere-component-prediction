import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sklearn
import joblib 

app = Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# ALLOWED_TYPES = (
    # "text", "number", "password", "email", "search",
    # "tel", "url", "range", "hidden",
# )
table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]


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
            ], justify = "start"),
            html.Hr(style= {'color': 'white'}),
            dbc.Row([
                dbc.Button(
            "Click me", id="example-button", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
            ])
        ],
                 className="app-card")
    ])
        , 
        dbc.Col([
            dbc.Table(table_header + table_body, bordered=True)
        ])
    ],
             className="div-space")
])

@app.callback(
    Output("out-temp", "children"), 
    Output("out-rel-hum", "children"), 
    Output("out-abs-hum", "children"), 
    Output("out-sens-1", "children"),
    Output("out-sens-2", "children"),
    Output("out-sens-3", "children"),
    Output("out-sens-4", "children"),
    Output("out-sens-5", "children"),
    Output("example-output", "children"), 
    [Input('input-temp', "value")],
    [Input('input-rel-hum', "value")],
    [Input('input-abs-hum', "value")],
    [Input("input-sens-1", "value")],
    [Input("input-sens-2", "value")],
    [Input("input-sens-3", "value")],
    [Input("input-sens-4", "value")],
    [Input("input-sens-5", "value")],
    [Input("example-button", "n_clicks")]
    )


# def cb_render(*vals):
    # sorcery skip: remove-redundant-fstring, simplify-fstring-formatting
    # return " | ".join((str(val) for val in vals if val))
def on_button_click(n):
    return "Not clicked." if n is None else f"Clicked {n} times."

if __name__ == '__main__':
    model = joblib.load("predModel.sav")
    app.run_server(debug=True)