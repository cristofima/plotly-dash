from dash import html, dcc
from dash.dependencies import Input, Output
import os

from app import app
from layouts import layout1, layout2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname: str):
    if pathname == '/dash/app1' or pathname == '/dash/app1/':
        return layout1.layout
    elif pathname == '/dash/app2' or pathname == '/dash/app2/':
        return layout2.layout
    else:
        return html.H1('Page Not Found')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run_server(host="0.0.0.0", port=port, debug=True)
