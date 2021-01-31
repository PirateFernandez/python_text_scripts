#import os
#import sys
import numpy as np
import mrcfile
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
filewithpath = '/Users/israel_CUMC/Documents/relion_files/ctffind_files/example.ctf'
filewithpath_split = filewithpath.split('/')
file_no_path = filewithpath_split[-1]
with mrcfile.open(filewithpath) as emd:
	nx, ny, nz = emd.header['nx'], emd.header['ny'], emd.header['nz']
	#x0, y0, z0 = emd.header['origin']['x'], emd.header['origin']['y'], emd.header['origin']['z']
	#x, y, z = np.float(x0), np.float(y0), np.float(z0)
	#dx, dy, dz = emd.voxel_size['x'], emd.voxel_size['y'], emd.voxel_size['z']
	#xyz = np.meshgrid(np.arange(x0, x0+nx*dx, dx), np.arange(y0, y0+ny*dy, dy), np.arange(z0, z0+nz*dz, dz), indexing='ij')
	#xyz_1 = np.asarray(xyz)
	#xyz_2 = xyz_1.reshape(3, nx*ny*nz)
	#xyz_3 = xyz_2.T
	only = emd.data.flatten(order='F').reshape(emd.header['nx'], emd.header['ny'])
	#only = emd.data.flatten(order='F').reshape(nx, ny, nz)
	#only_t = only.reshape(512, 512)
	#emd_to_show = xyz, emd.data.flatten(order='F').reshape(nx, ny, nz)

#print(f'nx:{nx}, ny:{ny}, nz:{nz}')
#print(f'x0={x0}, y0={y0}, z0={z0}')
#print(f'x,y,z: {x}, {y}, {z}')
#print(f'ds: dx={dx}, dy={dy}, dz={dz}')
#print(np.shape(xyz))
#print(np.shape(xyz))
#print(np.shape(xyz_1))
#print(np.shape(xyz_2))
#print(np.shape(xyz_3))
#print(np.shape(only))
#print(np.shape(only_t))
plt.imshow(only, cmap="binary")
plt.show()