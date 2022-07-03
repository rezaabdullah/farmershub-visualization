# import libraries
import pandas as pd
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
# from component import sign_in, navbar
import plotly.express as px
import plotly.graph_objects as go
from numerize import numerize
from src import load_data, sort_time, reorder

# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        'rel': 'stylesheet',
        'integrity': 'sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC',
        'crossorigin': 'anonymous'
    }
]

# instantiate the app
# _____________________________________________________________________________
# app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
#     meta_tags=[{"name":"viewport", "content":"width=device-width, initial-scale=1.0"}])
app = Dash(__name__, external_scripts=external_scripts,
                external_stylesheets=external_stylesheets,
                meta_tags=[{"name":"viewport",
                            "content":"width=device-width, initial-scale=1.0"}]
        )

# logo
LOGO = "assets/favicon.ico"

sign_in = dbc.Row(
    [
        dbc.Col(
            dbc.Button(
                "Sign in", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                sign_in,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="#1E6091", dark=True, expand=True
)

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# layout section: Bootstrap
# _____________________________________________________________________________
app.layout = dbc.Container([
    dbc.Row(navbar),
    dbc.Row("header", class_name="bg-primary"),
    dbc.Row("body"),
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)