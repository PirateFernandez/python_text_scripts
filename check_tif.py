###script to create a list of files in a directory and apply to them a bash command, capturing the output ans using it."""
import os 
import subprocess
dirpath = '/Users/israel_CUMC/Documents/python_training'
fileslist = os.listdir(dirpath)
tiflist = []
"""Standar loop with to choices to select files in the directory defined in dirpath."""
for i in fileslist:
	if '.py' in i:
		tiflist.append(i)
	elif '.pyc' in i:
		tiflist.append(i)
"""List comprehension to add the absolute path to the extracted files."""
listpathtif = [f"{dirpath}/{tiflist[i]}" for i in range(len(tiflist))]
"""Loop using the bash comand ls -l over the path/files stored in list."""
"""run subprocess is used within the loop and the stdout captured."""
"""stdout method is used to output the stdout and the decode method is used to generate a string stored in pcs."""
"""the ls -l output is splitted and the file size entry selected, transformed to int and used to select file larger than 1000 bytes."""
for i in listpathtif:
	pcs = subprocess.run(["ls", "-l", f"{i}"], stdout=subprocess.PIPE).stdout.decode("utf-8")
	#outputlist = pcs.stdout.decode("utf-8")
	pcs_split = pcs.split()
	number = int(pcs_split[4])
	if  number > 1000:
		print(i)
