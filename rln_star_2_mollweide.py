import os
import sys
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt 
try:
	filewithpath = sys.argv[1]
	
except IndexError:
	print("Wrong usage, please input absolute path to the star file.")
	print("Correct usage:")
	print("pythonn3.x rln_star_2_mollweide.py /path/path/relion_dir/Refine3D/jobxxx/run_class1.star")
	print("Please provide absolute path to file.")
	exit()
#filewithpath = '/Users/israel_CUMC/Desktop/C++/test_python/test_python/moll/run_ct15_data.star'
with open(filewithpath, 'r') as f:
	filelines = f.readlines()
filelines_crop = filelines[37:-1]
filelines_split = []
for i in filelines_crop:
	i_split = i.split()
	filelines_split.append(i_split)
rot = []
tilt = []
for i in filelines_split:
	rot.append(float(i[23]))
for i in filelines_split:
	tilt.append(float(i[24]))
tilt_m90 = [x -90 for x in tilt]
rot_rad = np.deg2rad(rot)
tilt_m90_rad = np.deg2rad(tilt_m90)
vertical_rad = np.vstack([tilt_m90_rad, rot_rad])
#m = gaussian_kde (vertical_rad)(vertical_rad)
plt.figure()
plt.subplot(111, projection="mollweide")
plt.scatter(rot_rad, tilt_m90_rad, s=10)
plt.grid(None)
plt.yticks(None)
plt.xticks([])
plt.yticks([])
plt.vlines(0,-1.5,1.5, linestyles='dotted')
plt.hlines(0,-10,10, linestyles='dotted')
plt.show()

