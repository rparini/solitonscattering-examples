### Show 'snapshot' of field at the boundary
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server

from snapshot.app import graph as snapshot_graph
from v95Kinematics.app import graph as v95_graph
graphs = {
	'snapshot': snapshot_graph, 
	'v95Kinematics': v95_graph
}

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(
        dcc.Tabs(children=[
        		dcc.Tab(label='Snapshot', value='snapshot'),
        		dcc.Tab(label='Kinematics v0=0.95', value='v95Kinematics'),
            ],
            value='snapshot',
            id='tabs',
            vertical=True,
            style={
                'height': '100vh',
                'borderRight': 'thin lightgrey solid',
                'textAlign': 'left'
            }
        ),
        style={'width': '20%', 'float': 'left'}
    ),
    html.Div(
        html.Div(id='tab-output'),
        style={'width': '80%', 'float': 'right'}
    )
])

@app.callback(Output('tab-output', 'children'), 
	[Input('tabs', 'value')]
)
def display_content(value):
    return html.Div([graphs[value]])

# Use plotly's css style sheet
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
