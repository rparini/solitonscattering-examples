import numpy as np
from scipy import pi
from matplotlib import pyplot as plt
import xarray as xr

from SolitonScattering import SG

dx = 0.025
dt = 0.02

xLim = [-40,0]
x0 = -20

M  = int((xLim[1] - xLim[0])/dx) + 1
x = np.linspace(xLim[0],xLim[1],M)

v0 = np.linspace(0.01, 0.99, 981) 	# step size 0.001
k  = np.linspace(0, 0.5, 501)		# step size 0.001

state = SG.kink(x,0,v0,x0,-1)
field = SG.SineGordon(state)
field.time_evolve('euler_robin', lambda v: 1000+abs(x0)/v, dt=dt, k=k, 
	dirichletValue=2*pi, 
	asymptoticBoundary={'L':2*pi},
	progressBar=True,
)

field.state.to_netcdf('Snapshot_t100_001.nc', engine='h5netcdf')

