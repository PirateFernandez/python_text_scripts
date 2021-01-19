import os
import sys
import time
import matplotlib.pyplot as plt
import mpld3
""" check if the user supplied path to motioncor log files, if not handle the exception."""
try:
	filepath_mcorr = sys.argv[1]
	
except IndexError:
	print("Wrong usage, please input absolute path to the motioncorr log files.")
	print("Correct usage:")
	print("pythonn3.x try_1_motioncorr_to_html.py /path/path/relion_dir/MotionCorr/jobxxx/imagename.log")
	print("Please provide absolute path.")
	exit()
"""check if the user supplied a resolution limit, if not handle the exception."""
#try:
#	filepath_ctffind4 = sys.argv[2]
#except IndexError:
#	print("Wrong usage, please input desired resolution limit.")
#	print("Correct usage:")
#	print("pythonn3.x ctfind4_sort_by_res.py /path/path/relion_dir/CtfFind/jobxxx/yyy res_limit")
#	print("Please provide a resolution limit.")
#	exit()

"""using os module, generate a list with all the files listed in the directory"""
"""initialize and fill other lists with only ctffind4.log files (list_2) and path+ctffind4.log (list_3)"""
def extract_x_displacement(filelistwithpath):
	x_displacement = []
	for i in filelistwithpath:
		with open(i, 'r') as f:
			f_lines = f.readlines()
			for i2 in f_lines:
				if 'Polynomial fit RMSD: X = ' in i2:
					i2_split = i2.split(" ")
					x_displacement.append(float(i2_split[5]))
	return x_displacement
def extract_y_displacement(filelistwithpath):
	x_displacement = []
	for i in filelistwithpath:
		with open(i, 'r') as f:
			f_lines = f.readlines()
			for i2 in f_lines:
				if 'Polynomial fit RMSD: X = ' in i2:
					i2_split = i2.split(" ")
					x_displacement.append(float(i2_split[9]))
	return x_displacement

#start_time = time.time()
#seconds = 4
#"""infinite while loop!!!"""
#while True:
#    current_time = time.time()
#    elapsed_time = current_time - start_time

#    if elapsed_time > seconds:
#		print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
file_list_mcorr = os.listdir(filepath_mcorr)
file_list_mcorr_2 = []
file_list_mcorr_2_path = []
		#print(file_list_mcorr)
"""loop to generate lists with only ctffind4.log files (list_2)"""
for i in file_list_mcorr:
	if '.log' in i:
		file_list_mcorr_2.append(i)
"""loop to generate list path+ctffind4.log (list_3)"""
for i in file_list_mcorr_2:
	file_list_mcorr_2_path.append(f"{filepath_mcorr}/{i}")
		
#for i in file_list_mcorr_2_path:	
x_mcorr_plot = extract_x_displacement(file_list_mcorr_2_path)
y_mcorr_plot = extract_y_displacement(file_list_mcorr_2_path)
x_lenght = [ i for i in range(1,(len(x_mcorr_plot)+1))]
y_lenght = [ i for i in range(1,(len(x_mcorr_plot)+1))]
fig, ax = plt.subplots(2, 1, sharey=True)
ax[0].scatter(x_lenght, x_mcorr_plot)
ax[0].set(xlabel='MotionCorr X displacement')
ax[0].plot(x_lenght, x_mcorr_plot)
ax[0].set(ylabel='RMSD')
ax[1].scatter(y_lenght, y_mcorr_plot)
ax[1].plot(y_lenght, y_mcorr_plot)
ax[1].set(xlabel='MotionCorr Y displacement')
#plt.show()
test = mpld3.fig_to_html(fig)	
write_html = '/home/ifernandez/Documents/python3_work/test.html'
with open(write_html, 'w') as f:
	f.write(test)