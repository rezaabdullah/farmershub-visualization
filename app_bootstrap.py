# import libraries
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# read dataset
df = pd.read_csv("clean_df.csv", dtype={"person_id":str, "person_name":str,
        "person_mobile":str, "person_gender":str}, parse_dates=["transaction_date", 
        "dropout_at"])

# instantiate the app
# _____________________________________________________________________________
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{"name":"viewport",
                            "content":"width=device-width, initial-scale=1.0"}]
                )

# layout section: Bootstrap
# _____________________________________________________________________________
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("eFarmersHub Playground", className="text-center text-primary mb-4"),
                width=12, className="bg-secondary")
    ),
    dbc.Row([
        dbc.Col(html.P("FILTER", className="text-center text-info"), width=2,
                className="bg-primary"),
        dbc.Col([
            dbc.Row([
                dbc.Col(html.P("CARD_1", className="text-center text-info mb-4"), width=2, className="border border-success"),
                dbc.Col(html.P("CARD_2", className="text-center text-info mb-4"), width=2, className="border border-success"),
                dbc.Col(html.P("CARD_3", className="text-center text-info mb-4"), width=2, className="border border-success"),
                dbc.Col(html.P("CARD_4", className="text-center text-info mb-4"), width=2, className="border border-success"),
                dbc.Col(html.P("CARD_5", className="text-center text-info mb-4"), width=2, className="border border-success"),
                dbc.Col(html.P("CARD_6", className="text-center text-info mb-4"), width=2, className="border border-success")
                ]),
            dbc.Row([
                dbc.Col(html.P("CHART_1", className="text-center text-info mb-4"), width=6, className="border border-success"),
                dbc.Col(html.P("CHART_2", className="text-center text-info mb-4"), width=6, className="border border-success"),
            ]),
            dbc.Row([
                dbc.Col(html.P("CHART_3", className="text-center text-info mb-4"), width=6, className="border border-success"),
                dbc.Col(html.P("CHART_4", className="text-center text-info mb-4"), width=6, className="border border-success"),
            ])
        ], width=10, className="bg-primary")
    ])
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)