### Show 'snapshot' of field at the boundary
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server

from snapshot.app import graph as snapshot_graph
from v95Kinematics.app import graph as v95_graph
from v875Kinematics.app import graph as v875_graph
graphs = {
	'snapshot': snapshot_graph, 
	'v95Kinematics': v95_graph,
	'v875Kinematics': v875_graph,
}

app.scripts.config.serve_locally = True

app.layout = html.Div([
	html.Div([
		html.P([
			"These examples have been created using the ", 
			html.A('solitonscattering', href='https://github.com/rparini/solitonscattering-examples'), 
			" library and replicate some of the figures in the paper ",
			html.A("Breaking integrability at the boundary: the sine-Gordon model with Robin boundary conditions", href='https://arxiv.org/abs/1509.08448'), 
			# html.A("Breaking integrability at the boundary: the sine-Gordon model with Robin boundary conditions", href='https://doi.org/10.1088/1751-8113/49/16/165205'), 
			# " by Robert Arthur, Patrick Dorey and Robert Parini, Journal of Physics A, Volume 49, Number 16, 2016, ",
			# html.A('(ArXiv:1509.08448)', href='https://arxiv.org/abs/1509.08448'), 
			".",
		]),
	    html.P(["The source code and data for these examples and this web app are hosted ", html.A('here', href='https://github.com/rparini/solitonscattering-examples'), '.']),
    ]),
    html.Div(
        dcc.Tabs(children=[
        		dcc.Tab(label='Snapshot', value='snapshot'),
        		dcc.Tab(label='Kinematics v0=0.95', value='v95Kinematics'),
        		dcc.Tab(label='Kinematics v0=0.875', value='v875Kinematics'),
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
    return html.Div(graphs[value])

# Use plotly's css style sheet
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
