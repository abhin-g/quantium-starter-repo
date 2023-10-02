import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read the CSV file
sales_data = pd.read_csv('processed_data.csv')

# Create a Dash web application
app = dash.Dash(__name__)

# Get unique regions from the "region" column
unique_regions = sales_data['region'].unique()

# Define the layout of the app with improved CSS styles
app.layout = html.Div([
    html.Div(
        html.H1("Sales Data Visualizer"),
        style={'textAlign': 'center', 'fontSize': 28, 'marginBottom': 20, 'color': 'navy'}
    ),
    
    # Create tabs for each region and an additional tab for "All Regions"
    dcc.Tabs(id="region-tabs", value=unique_regions[0], children=[
        dcc.Tab(label=region, value=region, style={'backgroundColor': 'lightgray', 'fontWeight': 'bold', 'border': '1px solid gray'}) for region in unique_regions
    ] + [dcc.Tab(label="All Regions", value="all", style={'backgroundColor': 'lightgray', 'fontWeight': 'bold', 'border': '1px solid gray'})]
    ),
    html.Div(id="line-chart-container", style={'margin': 20, 'backgroundColor': 'white', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)'}),
])

# Callback to update the line chart based on the selected region
@app.callback(
    dash.dependencies.Output("line-chart-container", "children"),
    [dash.dependencies.Input("region-tabs", "value")]
)
def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_data = sales_data
        title = 'Sales Over Time for All Regions'
    else:
        filtered_data = sales_data[sales_data['region'] == selected_region]
        title = f'Sales Over Time in {selected_region}'
    
    fig = px.line(filtered_data, x='date', y='sales', title=title)
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=20, r=20, t=50, b=50),
        title_x=0.5,  # Center the title horizontally
        title_y=0.9   # Adjust the vertical position of the title (0.5 is centered)
    )
    return dcc.Graph(figure=fig)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
