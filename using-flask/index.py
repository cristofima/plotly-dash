import os
from app import app
from dash import html
from layouts import layout1, layout2

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Dash using Flask'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
])


@server.route("/dash/<int:appId>/")
def dash_apps(appId: int):
    if appId == 1:
        app.layout = layout1.layout
    elif appId == 2:
        app.layout = layout2.layout
    else:
        app.layout = None

    return app.index()
