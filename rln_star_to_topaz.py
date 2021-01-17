"""python script to convert mamual o autopick particles coordinates files from Relion format to Topaz format."""
"""this rln_to_topaz.py scripts uses the class file RlnTopaz.py class, creating a instance of the class per rln particle file."""
"""this script takes as argument the full path to the directory where the xxx_manual.star or xxx_autopick.star files are located"""
"""usage: python3.x rln_star_to_topaz.py /folder/folder/project_folder_where_relion_gui_starts/ManualPick/jobxxx/xxxx"""
import os
from rlntotopaz2 import RlnToTopaz
import sys
try:
	filepath_1 = sys.argv[1]
	#filepath_1 !=''
except IndexError:
	print("Wrong usage, please input path to star files.")
	print("Correct usage:")
	print("pythonn3.x list_contents_dir.py /path/path/relion_dir/ManualPick/XXXX")
	exit()
file_list = os.listdir(filepath_1)
path_list = []
path_list_2 = []
path_list_3 = []
star_files = []
star_files_2 = []
to_write = 'image_name	x_coord	y_coord'
to_write_2 = ''
to_write_3 = ''
output = 'particles_topaz.txt'
for i in file_list:
	path_list = f"{filepath_1}/{i}"
	path_list_2.append(path_list)
star_files = []
for i in path_list_2:
	if 'manualpick.star' in i:
		path_list_3.append(i)
	elif 'autopick.star' in i:
		path_list_3.append(i)
		continue
for i in path_list_3:
	instance = RlnToTopaz(i)
	to_write_2 += instance.open_and_liner()
	to_write_3 = f"{to_write}\n{to_write_2}"
with open(output, 'w') as object_file:
	object_file.write(to_write_3)

