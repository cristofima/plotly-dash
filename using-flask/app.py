import dash
from flask import Flask

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/',
    suppress_callback_exceptions=True
)
