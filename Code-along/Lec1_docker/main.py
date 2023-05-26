#%%
import plotly_express as px
import numpy as np
from dash import Dash, dcc, Output, Input
from dash.html import H1, H2, Div, P

dropdown_options = [{
    "label": f"{rolls} rolls",
    "value": rolls}
    for rolls in [10, 100, 1000, 10000]]
#%%
app = Dash(__name__)

app.layout = Div([
    H1('Dice simulator'),
    P('Choose number of dices and number of rolls'),
    dcc.Graph(id = 'dice-graph'),
    H2('Number of rolls'),
    dcc.Dropdown(id = 'number-rolls', options = dropdown_options, value = 10),
    H2('Number of dices'),
    dcc.Slider(id = 'number-dices', min = 1, max = 6, value = 2, step = 1),
])

@app.callback(Output('dice-graph', 'figure'), Input('number-rolls', 'value'), Input('number-dices', 'value'))

def dice_simulator_histogram(rolls, number_dices):
    dices = np.random.randint(1, 7, (rolls, number_dices)) # rolls = rows, number_dices = columns
    return px.histogram(dices.sum(axis = 1)) # sum(axis = 1) = summing over columns

if __name__ == '__main__':
    print('Hello from the docker side')

    app.run_server(debug=True)