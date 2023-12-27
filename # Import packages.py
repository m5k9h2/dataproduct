# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from io import StringIO

# Fetch historical data
import yfinance as yf

# Use the correct ticker symbol for gold, for example, 'GC=F' (Gold Futures)
gold_ticker = 'GC=F'
df = yf.download(gold_ticker, start="2022-01-01", end="2023-12-22")
df.head()

# Initialize the app
app = Dash(__name__)

   
# App layout
app.layout = html.Div([
    html.Div(children='App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['High', 'Close', 'Low'], value='Close', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(df, x='Date', y=col_chosen)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)