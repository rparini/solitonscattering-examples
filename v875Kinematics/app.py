### Show 'snapshot' of field at the boundary
import xarray as xr
import numpy as np
from numpy import pi
import os 

import dash
import dash_core_components as dcc
import dash_html_components as html

dir_path = os.path.dirname(__file__)
if dir_path:
    dir_path += '/'
arrayFile = dir_path + 'v875Kinematics_k201_t1000_dx025_dt02_eigenvalues.nc'

with xr.open_dataset(arrayFile, engine='h5netcdf') as eigenvalues:
    from SolitonScattering import SG
    eigenvalues = SG.ScatteringData(eigenvalues)
    typed_kinematics = eigenvalues.typed_kinematics()

graph = dcc.Graph(
    id='v95Kinematics',
    figure={
        'data': [{
            'x': eigenvalues.data['k'].data, 
            'y': typed_kinematics['Kink']['speed'][:,0], 
            'name': 'Kink',
            'line': {'color':'#1f77b4'},
        },
        {
            'x': eigenvalues.data['k'].data, 
            'y': typed_kinematics['Antikink']['speed'][:,0], 
            'name': 'Antikink',
            'line': {'color':'#d62728'},
        },
        {
            'x': eigenvalues.data['k'].data, 
            'y': typed_kinematics['Breather']['speed'].data, 
            'name': 'Breather Speed',
            'line': {'color':'#2ca02c'},
        },
        {
            'x': eigenvalues.data['k'].data, 
            'y': typed_kinematics['Breather']['frequency'].data, 
            'name': 'Breather Frequency',
            'line': {'color':'black', 'dash':'dash'},
        },
        ],
        'layout': {
            'xaxis': {
                'title':'Defect Parameter, k', 
            },
            'yaxis': {
                'title':'Speed/Frequency', 
                'range':[0,1],
            },
            'title': "Kinematics for v0=0.95",
        },
    }
)

if __name__ == '__main__':
    app = dash.Dash()
    server = app.server
    app.layout = html.Div(children=[graph])
    app.run_server(debug=True)
