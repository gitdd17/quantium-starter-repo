import dash
from dash import html
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Hello Quantium!", style={"textAlign": "center"}),
    html.P("Your Dash environment is set up correctly 🎉")
])
if __name__ == "__main__":
    app.run(debug=True)

