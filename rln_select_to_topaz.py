
import os 
import sys
#filepath = '/Users/israel_CUMC/Documents/python_work/100_lines.star'
"""python script to convert particles coordinates from a Select Relion job to Topaz format."""
"""usage: python3.x rln_select_to_topaz.py /folder/folder/project_folder_where_relion_gui_starts/Select/jobxxx/particles.star"""
try:
	filepath = sys.argv[1]
	#filepath_1 !=''
except IndexError:
	print("Wrong usage, please input path to the Select star file.")
	print("Correct usage:")
	print("pythonn3.x rln_select_to_topaz.py /path/path/relion_dir/Select/jobXXX/particles.star")
	exit()
with open(filepath, 'r') as object_file:
			file_lines = object_file.readlines()
			file_lines_clean = []
			for i in file_lines:
				if i != '\n' and len(i) >=5:
					file_lines_clean.append(i)
			ptc_lines = []
			for i in file_lines_clean:
				if "@" in i:
					ptc_lines.append(i)
			x_coord = []
			for i in ptc_lines:
				i_split = i.split()
				x_coord.append(i_split[0])
			y_coord = []
			for i in ptc_lines:
				i_split = i.split()
				y_coord.append(i_split[1])
			img_name = []
			for i in ptc_lines:
				i_split = i.split()
				img_name.append(i_split[5])
			img_name_trim = []
			for i in img_name:
				i_split = i.split('/')
				img_name_trim.append(i_split[-1])
			img_name_trim_2 = []
			for i in img_name_trim:
				i_split = i.split('.')
				img_name_trim_2.append(i_split[-2])
			header = 'image_name	x_coord	y_coord\n'
			for i in range(len(ptc_lines)):
				header += f"{img_name_trim_2[i]}\t{x_coord[i]}\t{y_coord[i]}\n"
			to_write = 'particles_topaz.txt'
			with open(to_write, 'w') as f:
				f.write(header)
			print("Done! particles_topaz.txt file written.")


				
