# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# https://coolors.co/d8f3dc-b7e4c7-95d5b2-74c69d-52b788-40916c-2d6a4f-1b4332-081c15
# https://coolors.co/007f5f-2b9348-55a630-80b918-aacc00-bfd200-d4d700-dddf00-eeef20-ffff3f
# https://coolors.co/d9ed92-b5e48c-99d98c-76c893-52b69a-34a0a4-168aad-1a759f-1e6091-184e77
# #f9f4ee

from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="header",
            children=html.H1("eFarmersHub", className="header--title")
        ),
        html.Div(
            className="container-body",
            children=[
                html.Div(
                    "FILTER",
                    className="container-body--filter",
                ),
                html.Div(
                    className="container-body--chart",
                    children=[
                        html.Div(
                            className="container-body--card",
                            children=[
                                html.Div("Card_1", className="container-card"),
                                html.Div("Card_2", className="container-card"),
                                html.Div("Card_3", className="container-card"),
                                html.Div("Card_4", className="container-card"),
                                html.Div("Card_5", className="container-card"),
                                html.Div("Card_6", className="container-card"),                                
                            ]
                        ),
                        html.Div(
                            className="container-chart",
                            children=[
                                html.Div(
                                    className="container-chart--row",
                                    children=[
                                        html.Div("Graph_1", className="container-graph"),
                                        html.Div("Graph_2", className="container-graph")
                                    ]
                                ),
                                html.Div(
                                    className="container-chart--row",
                                    children=[
                                        html.Div("Graph_3", className="container-graph"),
                                        html.Div("Graph_4", className="container-graph")
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
