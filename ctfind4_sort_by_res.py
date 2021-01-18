import os
import sys
""" check if the user supplied path to log files, if not handle the exception."""
try:
	filepath_1 = sys.argv[1]
	
except IndexError:
	print("Wrong usage, please input path to ctfind4.log files.")
	print("Correct usage:")
	print("pythonn3.x ctfind4_sort_by_res.py /path/path/relion_dir/CtfFind/jobxxx/yyy res_limit")
	print("Please provide a directory path.")
	exit()
"""check if the user supplied a resolution limit, if not handle the exception."""
try:
	resolution_limit = float(sys.argv[2])
except IndexError:
	print("Wrong usage, please input desired resolution limit.")
	print("Correct usage:")
	print("pythonn3.x ctfind4_sort_by_res.py /path/path/relion_dir/CtfFind/jobxxx/yyy res_limit")
	print("Please provide a resolution limit.")
	exit()

"""using os module, generate a list with all the files listed in the directory"""
"""initialize and fill other lists with only ctffind4.log files (list_2) and path+ctffind4.log (list_3)"""
file_list = os.listdir(filepath_1)
file_list_2 = []
file_list_3 = []
"""loop to generate lists with only ctffind4.log files (list_2)"""
for i in file_list:
	if '_ctffind4.log' in i:
		file_list_2.append(i)
"""loop to generate list path+ctffind4.log (list_3)"""
for i in file_list:
	if '_ctffind4.log' in i:
		i2 = f"{filepath_1}/{i}"
		file_list_3.append(i2)
"""define a function to extract the resolution line from ctffind4.log's"""
"""input is a list of path+ctffind4.log and it returns a list of lines 'Thon rings with good fit up to  : XXXX'"""
def extract_res_line(logfilelist):
	res_list = []
	for i in logfilelist:
		with open(i, 'r') as object_file:
			file_lines = object_file.readlines()
			for i2 in file_lines:
				if 'Thon rings with good fit up to  :' in i2:
					res_list.append(i2)
	return res_list
"""using function extract_res_line() store the list of lines with resolution values in list res_list_2"""
res_list_2 = extract_res_line(file_list_3)
"""generate a list with only the res values followed by Angstroms"""
res_list_3 = []
for i in res_list_2:
	i_split = i.split(":")
	res_list_3.append(i_split[-1])
"""create a dictionary from two lists"""
"""maps name of the ctffind4.log to the res value"""
dic_img_res = dict(zip(file_list_2, res_list_3))
"""print in a nice format the key and values from dict dic_img_res"""
#for key, value in dic_img_res.items():
	#print((f"{key} {value}").strip())
"""generate a list of floats with the res values"""
res_list_4 = []
for i in res_list_3:
	i_split = i.split(" ")
	res_list_4.append(float(i_split[-2]))
"""generate a second dictionary mapping log file names (str) to res (floats)"""
dic_img_res_2 = dict(zip(file_list_2, res_list_4))
"""print only those logs files with resolution values better than the especified res number"""
for key, value in dic_img_res_2.items():
	if value < resolution_limit:
		print((f"Image {key} reach resolution beyond {resolution_limit}.").strip())
