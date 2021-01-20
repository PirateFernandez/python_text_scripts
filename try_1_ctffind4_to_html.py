import os
import sys
import time
import matplotlib.pyplot as plt
import mpld3
""" check if the user supplied path to motioncor log files, if not handle the exception."""
try:
	filepath_ctffind4 = sys.argv[1]
except IndexError:
	print("Wrong usage, please input desired resolution limit.")
	print("Correct usage:")
	print("pythonn3.x ctfind4_sort_by_res.py /path/path/relion_dir/CtfFind/jobxxx/yyy res_limit")
	print("Please provide a resolution limit.")
	exit()

def extract_defocus_1(filelistwithpath):
	defocus_1 = []
	defocus_1_um = []
	for i in filelistwithpath:
		with open(i, 'r') as f:
			f_lines = f.readlines()
			for i2 in f_lines:
				if 'Estimated defocus values        :' in i2:
					i2_split = i2.split(" ")
					defocus_1.append(float(i2_split[11]))
	defocus_1_um = [i/10000 for i in defocus_1]
	return defocus_1_um

def extract_defocus_2(filelistwithpath):
	defocus_2 = []
	defocus_2_um = []
	for i in filelistwithpath:
		with open(i, 'r') as f:
			f_lines = f.readlines()
			for i2 in f_lines:
				if 'Estimated defocus values        :' in i2:
					i2_split = i2.split(" ")
					defocus_2.append(float(i2_split[13]))
	defocus_2_um = [i/10000 for i in defocus_2]
	return defocus_2_um

def avg_defocus(listdefocus1, listdefocus2):
	avg_defocus_list = []
	for i in range(0, len(listdefocus1)):
		i_avg = (listdefocus1[i]+listdefocus2[i])/2
		avg_defocus_list.append(i_avg)
	return avg_defocus_list

while True:
	time.sleep(2)
	file_list_all = os.listdir(filepath_ctffind4)
	file_list_ctffind4_log = []
	file_list_ctffind_4_log_with_path = []
	"""loop to generate lists with only ctffind4.log files (list_2)"""
	for i in file_list_all:
		if 'ctffind4.log' in i:
			file_list_ctffind4_log.append(i)
	"""loop to generate list path+ctffind4.log (list_3)"""
	for i in file_list_ctffind4_log:
		file_list_ctffind_4_log_with_path.append(f"{filepath_ctffind4}/{i}")	
	list_defocus_1 = extract_defocus_1(file_list_ctffind_4_log_with_path)
	list_defocus_2 = extract_defocus_2(file_list_ctffind_4_log_with_path)

	avg_defocus_glob = avg_defocus(list_defocus_1, list_defocus_2)
	avg_defocus_glob_2f = []
	for i in avg_defocus_glob:
		i2 = float(f"{i:.2f}")
		avg_defocus_glob_2f.append(i2)
	x_defocus_1 = [ i for i in range(1,(len(list_defocus_1)+1))]
	x_defocus_2 = [ i for i in range(1,(len(list_defocus_2)+1))]
	x_defocus_avg = [ i for i in range(1,(len(avg_defocus_glob_2f)+1))]

	copy_avg_all = avg_defocus_glob_2f[:]
	last_10_avg = []
	last_10_sum = 0
	if len(copy_avg_all) > 11: 
		while len(copy_avg_all) > 10:
			last_10 = copy_avg_all[-10:-1]
			last_10_avg.append((sum(last_10))/10)
			copy_avg_all.pop()
	
	#print(last_10_avg)

	fig, ax = plt.subplots(3, 2, sharey=True)
	
	ax[0,0].scatter(x_defocus_1, list_defocus_1, s=2)
	ax[0,0].set(ylabel='Defocus 1 (um)')
	ax[0,0].plot(x_defocus_1, list_defocus_1, linewidth=1)

	ax[0,1].scatter(range(1,len(last_10_avg)+1), last_10_avg, s=2)
	ax[0,1].set(ylabel='Average defocus last 10 images (um)')
	ax[0,1].plot(range(1,len(last_10_avg)+1), last_10_avg, linewidth=1)

	ax[1,0].scatter(x_defocus_2, list_defocus_2, s=2)
	ax[1,0].set(ylabel='Defocus 2 (um)')
	ax[1,0].plot(x_defocus_2, list_defocus_2, linewidth=1)

	ax[2,0].scatter(x_defocus_avg, avg_defocus_glob_2f, s=2)
	ax[2,0].set(ylabel='Defocus avg (um)')
	ax[2,0].plot(x_defocus_avg, avg_defocus_glob_2f, linewidth=1)
	ax[2,0].set(xlabel='Image Number')
	#plt.show()
	html_obj = mpld3.fig_to_html(fig)	
	write_html = '/home/ifernandez/Documents/python3_work/ctffind4_live.html'
	with open(write_html, 'w') as f:
		f.write(html_obj)
	plt.close(fig)