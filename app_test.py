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

df = pd.read_csv("clean_df.csv", dtype={"person_id":str, "person_name":str,
    "person_mobile":str, "person_gender":str}, parse_dates=["transaction_date", 
    "dropout_at"])

# get indicator
def get_indicator():
    fig = go.Figure(go.Indicator(
            mode = "number",
            value = df["user_id"].nunique(),
            number = {"font":{"size":20}},
            title={"text":"Number of<br>Franchisee",
                "font":{"size":15}
            },
            domain = {'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        margin={"t":40, "l":0, "b":0, "r":0}
    )

    return fig
# def get_indicator():
#     # create figure object
#     fig = go.Figure()

#     # add trace
#     fig.add_trace(
#         go.Indicator(
#             value=df["user_id"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>FarmersHub"},
#             domain={"row":0, "column": 0}
#         )
#     )

#     fig.add_trace(
#         go.Indicator(
#             value=df["country_name"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>Countries"},
#             domain={"row":0, "column": 1}
#         )
#     )

#     fig.add_trace(
#         go.Indicator(
#             value=df["parent_name"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>Franchisee"},
#             domain={"row":0, "column": 2}
#         )
#     )

#     fig.add_trace(
#         go.Indicator(
#             value=df["user_id"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>FarmersHub"},
#             domain={"row":0, "column": 3}
#         )
#     )

#     fig.add_trace(
#         go.Indicator(
#             value=df["country_name"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>Countries"},
#             domain={"row":0, "column": 4}
#         )
#     )

#     fig.add_trace(
#         go.Indicator(
#             value=df["parent_name"].nunique(),
#             mode="number",
#             title={"text":"Number of<br>Franchisee"},
#             domain={"row":0, "column": 5}
#         )
#     )

#     fig.update_layout(
#         grid = {'rows': 1, 'columns': 6, 'pattern': "independent"},
#         template = {"data": {"indicator": [{
#             "title":{"font":{"size":15}},
#             "number":{"font":{"size":20}}}]}},
#         margin={"t":30, "l":0, "b":0, "r":0})

#     return fig

def get_revenue():
    df_time = df.groupby(["transaction_date"]).agg(revenue_usd=("revenue_usd", "sum")).reset_index()
    fig = px.line(df_time, x="transaction_date", y="revenue_usd")
    fig.update_layout(
        margin=dict(l=0, r=10, t=20, b=0)
    )
    return fig

def get_geomap():
    df_geomap = df.groupby("country_name").agg(revenue_usd=("revenue_usd", "sum"),
            transaction_count=("user_id", pd.Series.nunique),
            user_count=("user_id", pd.Series.nunique)).reset_index()
    iso_map = {"Bangladesh": "BGD", "Indonesia": "IDN", "Kenya": "KEN", "Mali": "MLI",
        "Nigeria": "NGA", "Senegal": "SEN"}
    df_geomap["iso_alpha"] = df_geomap["country_name"].map(iso_map)
    

    fig = px.choropleth(df_geomap, locations="iso_alpha", color="user_count",
        hover_name="country_name", color_continuous_scale=px.colors.sequential.RdPu)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

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
                                # html.Div("Metric_1", className="container-card"),
                                # html.Div("Metric_1", className="container-card"),
                                # html.Div("Metric_1", className="container-card"),
                                # html.Div("Metric_1", className="container-card"),
                                # html.Div("Metric_1", className="container-card"),
                                # html.Div("Metric_1", className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={"width": "100%", "height":"100%"}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                                # html.Div(dcc.Graph(figure=get_indicator(), style={'width': "100%", 'height': "100%", 'display': 'inline-block'}), className="container-card"),
                            ]
                        ),
                        html.Div(
                            className="container-chart",
                            children=[
                                html.Div(
                                    className="container-chart--row",
                                    children=[
                                        # html.Div("Graph_1", className="container-graph"),
                                        html.Div(
                                            dcc.Graph(
                                                id="Graph_1",
                                                # responsive=True,
                                                figure=get_revenue(),
                                                style={'width': "100%", 'height': "100%", 'display': 'inline-block'}
                                            ),
                                            className="container-graph"
                                        ),
                                        # html.Div("Graph_2", className="container-graph")
                                        html.Div(
                                            dcc.Graph(
                                                id="Graph_2",
                                                # responsive=True,
                                                figure=get_geomap(),
                                                style={'width': "100%", 'height': "100%", 'display': 'inline-block'}
                                            ),
                                            className="container-graph"
                                        )
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
