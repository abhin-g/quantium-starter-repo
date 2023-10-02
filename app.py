import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read only the "date" and "sales" columns from a CSV file
sales_data = pd.read_csv('processed_data.csv', usecols=['date', 'sales'])

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.Div(
        html.H1("Sales Data Visualizer", style={'textAlign': 'center', 'color': 'navy'}),  # Centered and blue header
    ),

    dcc.Graph(
        id='line-chart',
        figure=px.line(sales_data, x='date', y='sales', title='Sales Over Time')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
