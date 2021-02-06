import re
import os
import sys
import numpy as np
import scipy
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt 
#filewithpath = '/Users/israel_CUMC/Desktop/MATPLOTLIB/run_ct15_data_1000lines.star'
"""check if user supplied an absolute path with star file to plot, if not handle the exception."""
try:
	filewithpath = sys.argv[1]
	
except IndexError:
	print("Wrong usage, please input absolute path to the star file.")
	print("Correct usage:")
	print("pythonn3.x rln_star_2_mollweide.py /path/path/relion_dir/Refine3D/jobxxx/run_class1.star")
	print("Please provide absolute path to file.")
	exit()
"""open file object and create a list of lines."""	
with open(filewithpath, 'r') as f:
	filelines_pre = f.readlines()
"""remove the first 4 lines and the last empty one."""
filelines = filelines_pre[4:-2]
"""split the list of lines into header with are lines starting with '_rln...' and lines starting with a number that each belong to an aligned particle."""
filelines_header = []
filelines_body = []
for i in filelines:
	if i.startswith('_rln'):
		filelines_header.append(i)
for i in filelines:
	if i[1].isdigit():
		filelines_body.append(i) 
"""remove empty lines."""
filelines_header_clean = [ i.strip() for i in filelines_header]
filelines_body_clean = [ i.strip() for i in filelines_body]
rot_column = 0
tilt_column = 0
"""Look for column of the star file expecifiying the rot and tilt column."""
for i in filelines_header_clean:
	if '_rlnAngleRot' in i:
		rot_column_list = i.split("#")
		rot_column = (int(rot_column_list[-1]))-1
for i in filelines_header_clean:
	if '_rlnAngleTilt' in i:
		tilt_column_list = i.split("#")
		tilt_column = (int(tilt_column_list[-1]))-1
"""extract rot and tilt values from the identified columns values."""
rot = []
tilt = []
for i in filelines_body_clean:
	i_split = i.split()
	rot.append(float(i_split[rot_column]))
for i in filelines_body_clean:
	i_split = i.split()
	tilt.append(float(i_split[tilt_column]))
"""shift tilt values 90 degrees and transform them to radians as well as rot vaules."""
tilt_m90 = [x -90 for x in tilt]
rot_rad = np.deg2rad(rot)
tilt_m90_rad = np.deg2rad(tilt_m90)
"""create a vertical numpy array with the values on radians."""
vertical_rad = np.vstack([tilt_m90_rad, rot_rad])
"""use scipy gaussian kde function to calculate the density function using the vertical numpy stack."""
m = gaussian_kde (vertical_rad)(vertical_rad)
"""plotting"""
plt.figure()
plt.subplot(111, projection="mollweide")
plt.scatter(rot_rad, tilt_m90_rad, cmap='plasma', c=m, s=5)
plt.grid(None)
plt.xticks([])
plt.yticks([])
plt.vlines(0,-1.6,1.6, colors='k', linestyles='dashed')
plt.hlines(0,-10,10, colors='k', linestyles='dashed')
plt.savefig('/path/file.png', dpi=300)
plt.show()


