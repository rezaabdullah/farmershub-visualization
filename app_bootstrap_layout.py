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

# num_user = numerize.numerize(df["user_id"].nunique())
# total_revenue = numerize.numerize(df["revenue_usd"].sum())
# gross_profit = numerize.numerize(df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
#     - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum())
# gross_profit_margin = numerize.numerize((df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
#     - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()) /
#     df["revenue_usd"].sum()) + "%"
# net_profit = numerize.numerize(df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
#     - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()
#     - df.query("transaction_category == 'Indirect Cost'")["expenditure_usd"].sum())
# net_profit_margin = numerize.numerize((df["revenue_usd"].sum() - df["cogs_amount_usd"].sum()
#     - df.query("transaction_category == 'Direct Cost'")["expenditure_usd"].sum()
#     - df.query("transaction_category == 'Indirect Cost'")["expenditure_usd"].sum()) /
#     df["revenue_usd"].sum()) + "%"

# def get_revenue():
#     df_time = df.groupby(["transaction_date"]).agg(revenue_usd=("revenue_usd", "sum")).reset_index()
#     fig = px.line(df_time, x="transaction_date", y="revenue_usd")
#     fig.update_layout(
#         margin=dict(l=0, r=10, t=20, b=0)
#     )
#     return fig


# instantiate the app
# _____________________________________________________________________________
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{"name":"viewport",
                            "content":"width=device-width, initial-scale=1.0"}]
        )

# layout section: Bootstrap
# _____________________________________________________________________________
app.layout = dbc.Container([
    dbc.Row("header", class_name="container-main"),
    dbc.Row("body"),
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)