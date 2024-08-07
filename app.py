from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

app.layout = [
    # j'ai besoin d'une balise h1 avec un titre et un design css
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    # j'ai besoin d'une liste déroulante qui prend ses elements depuis le dataframe
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    # j'ai besoin d'une courbe representant mes données
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value): # une fonction qui me permet de saisir le nom d'un pays
    dff = df[df.country==value]
    # et rafraichir la courbe en fonction du nom qui a été saisi
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)

