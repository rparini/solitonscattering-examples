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

### Make and save field
import xyzpy as xyz
def tevolve(v, k):
	state = SG.kink(x,0,v,x0,-1)
	field = SG.SineGordon(state)
	field.time_evolve('euler_robin', 100+abs(x0)/v, dt=dt, k=k, dirichletValue=2*pi, asymptoticBoundary={'L':2*pi},
		progressBar=False)
	return float(field.state['u'][{'x':-1}].data)

r = xyz.Runner(tevolve, 
		var_names = ['u'], 
		# var_coords = {'x':x}	# XXX: Issue is we don't know x before tevolve is run!  So we'll just save u at boundary for now.
	)

combos = [('v', v0), ('k', k)]
result = r.run_combos(combos, parallel=True, verbosity=2)
result.to_netcdf('Snapshot_xyz_t100_001.nc', engine='h5netcdf')

