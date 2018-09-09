### Show 'snapshot' of field at the boundary
import xarray as xr
import numpy as np
from numpy import pi

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server

arrayFile = 'Array_xyz_01.nc'

with xr.open_dataset(arrayFile, engine='h5netcdf') as state:
	if 'x' in state.dims:
		u0 = state['u'][{'x':-1}]
	else:
		u0 = state['u']
	u0 = u0.transpose('v', 'k')

	data = np.array([[1, 2.1, 3], [3,4,0]])

	app.layout = html.Div(children=[
	    html.H1(children='Snapshot'),

	    # html.Div(children='''
	    #     Dash: A web application framework for Python.
	    # '''),

	    dcc.Graph(
	        id='example-graph',
	        figure={
	            'data': [{
	            	'x': u0['k'].data, 
	            	'y': u0['v'].data, 
	            	'z': u0.data, 
	            	'type': 'heatmap', 
	            	'colorscale': 'Jet',
	            	'zmin': -pi,
	            	'zmax': 4*pi,
	            	'colorbar': {
	            		'title': 'u(0,tf)', 
	            		'ticktext': ['-pi', '0', 'pi', '2pi', '3pi', '4pi'],
	            		'tickvals': [-pi, 0, pi, 2*pi, 3*pi, 4*pi],
	            	},
	            }],
	            'layout': {
	            	'height': 800,
	            	'width': 500,
	            	'xaxis': {
	            		'title':'Defect Parameter, k', 
	            		'tickvals':[0,0.1,0.2,0.3,0.4,0.5],
	            	},
	            	'yaxis': {
	            		'title':'Initial Soliton Velocity, v0', 
	            		'range':[0,1],
	            		'tickvals':[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1],
	            		'scaleanchor': 'x', 
	            		'scaleratio': 1,
	            	},
	                'title': "'Snapshot' of the field value at x=0 and t=100+|x0|/v0",
	                'scene': {'aspectmode': "data"},
	            },
	        }
	    )
	])

if __name__ == '__main__':
    app.run_server(debug=True)
