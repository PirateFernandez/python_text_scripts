import numpy as np
import mrcfile
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from PIL import Image
"""Using mrcfile python package, open .ctf as mrc python obbject"""
"""In this simple case supply a pathfile with a variable."""
filewithpath = '/home/ifernandez/Documents/relion_examples/ctffind_files_jinfan/20feb09a_Jinfan_1_KriosC1_Feb_09_2020_00007Gr_00003Sq_v03_00022Hln_00009Enn_frames_PS.ctf'
"""after opening, using mrcfile.header, extract the dimensions of the image"""
"""Generate a numpy array with the dimensions of the mrc file and assing values with mrcfile pacakage data function."""
with mrcfile.open(filewithpath) as emd:
	nx, ny, nz = emd.header['nx'], emd.header['ny'], emd.header['nz']
	ctf_np_512 = emd.data.flatten(order='F').reshape(emd.header['nx'], emd.header['ny'])
"""Simple way of scaling down images by reshaping the numpy array and averaging groups of values."""
ctf_np_256_reshaped = np.reshape(ctf_np_512, (256, 2, 256, 2)) 
"""numpy mean function can average over two dimension if a tuple is supplied with axes to use."""
ctf_np_256 = np.mean(ctf_np_256_reshaped, (1, 3))
ctf_np_128_reshaped = np.reshape(ctf_np_512, (128, 4, 128, 4))
ctf_np_128 = np.mean(ctf_np_128_reshaped, (1, 3)) 
"""Plot in one figure with three subpanels the ctf image full size, bin2 and bin4 with diffrent color-maps."""
fig = plt.figure()
ax_0 = fig.add_subplot(1, 3, 1)
imgplot = plt.imshow(ctf_np_512, cmap='binary')
ax_0.set_title('CTF 512')
ax_0.set_xticks([])
ax_0.set_yticks([])
#####
ax_1 = fig.add_subplot(1, 3, 2)
imgplot = plt.imshow(ctf_np_256, cmap='cool')
ax_1.set_title('CTF 256')
ax_1.set_xticks([])
ax_1.set_yticks([])
#####
ax_2 = fig.add_subplot(1, 3, 3)
imgplot = plt.imshow(ctf_np_128, cmap='cividis')
ax_2.set_title('CTF 128')
ax_2.set_xticks([])
ax_2.set_yticks([])
plt.show()
