# import libraries
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from numerize import numerize
from src import load_data, sort_time, reorder

df = load_data()
df = sort_time(df)
df = reorder(df)

num_user = numerize.numerize(df["user_id"].nunique())
total_revenue = numerize.numerize(df["revenue_usd"].sum())
gross_profit = numerize.numerize(df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
    - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum())
gross_profit_margin = numerize.numerize((df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
    - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()) /
    df["revenue_usd"].sum()) + "%"
net_profit = numerize.numerize(df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
    - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()
    - df.query("transaction_category == 'Indirect Cost'")["expenditure_usd"].sum())
net_profit_margin = numerize.numerize((df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
    - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()
    - df.query("transaction_category == 'Indirect Cost'")["expenditure_usd"].sum()) /
    df["revenue_usd"].sum()) + "%"

def get_revenue():
    df_time = df.groupby(["transaction_date"]).agg(revenue_usd=("revenue_usd", "sum")).reset_index()
    fig = px.line(df_time, x="transaction_date", y="revenue_usd")
    fig.update_layout(
        margin=dict(l=0, r=10, t=20, b=0)
    )
    return fig


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
                width=12)
    ),
    dbc.Row([
        dbc.Col(html.P("FILTER", className="text-center text-info"), width=2,
                className="bg-primary"),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Revenue", class_name="font-weight-bold"),
                    dbc.CardBody(html.H4("$" + str(total_revenue), className="card-title text-primary"))
                ], class_name="shadow-lg rounded")),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Total Users"),
                    dbc.CardBody(html.H4(str(num_user), className="card-title text-primary"))
                ], class_name="shadow-lg rounded")),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Gross Profit"),
                    dbc.CardBody(html.H4("$" + str(gross_profit), className="card-title text-primary"))
                ], class_name="shadow-lg rounded")),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Gross Profit (%)"),
                    dbc.CardBody(html.H4("$" + str(gross_profit_margin), className="card-title text-primary"))
                ], class_name="shadow-lg rounded")),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Net Profit"),
                    dbc.CardBody(html.H4("$" + str(net_profit), className="card-title text-primary"))
                ], class_name="shadow-lg rounded")),
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Net Profit (%)"),
                    dbc.CardBody(html.H4("$" + str(net_profit_margin), className="card-title text-primary"))
                ], class_name="shadow-lg rounded"))
                # dbc.Col(dbc.CardBody(class_name="shadow-lg rounded"))
            ], class_name="mb-4"),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id="timeseries_1",
                        # responsive=True,
                        figure=get_revenue(),
                        # style={"width": "100%"}
                        className="shadow-lg rounded"
                    ), width=6),
                dbc.Col(
                    dcc.Graph(
                        id="timeseries_2",
                        responsive=True,
                        figure=get_revenue(),
                        className="shadow-lg rounded"
                    ), width=6)
            ], class_name="mb-4"),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id="timeseries_3",
                        responsive=True,
                        figure=get_revenue(),
                        className="shadow-lg rounded"
                    ), width=6),
                dbc.Col(
                    dcc.Graph(
                        id="timeseries_4",
                        responsive=True,
                        figure=get_revenue(),
                        className="shadow-lg rounded"
                    ), width=6)
            ])
        ], width=10)
    ])
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)