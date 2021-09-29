import os 
import subprocess
###
def number_split(filename):
	filename_split_1 = filename.split("_")
	filename_split_2 = filename_split_1[-1].split(".")
	return int(filename_split_2[-2])
###
#pcs = subprocess.run(["mv", f"{i}"], f"{current[-2]}_g0.tif")
dirpath = '/cryoem-data3/ISF/ApoFe_200kev_sept/tiff'
####you have to place here the absolute path to the directory where the tif files are located and execute this script in the same directory###
fileslist = os.listdir(dirpath)
###little loop ove the contains of the filelist list to extract only tif files###
tiflist = []
for i in fileslist:
	if '.tif' in i:
		tiflist.append(i)
###in this case I want to rename each file sequentially in batches of 9 as we took 3x3=9 images per stage shift in serial EM. I create 9 different list of numbers
### each outstepped by 1 and then I will compare the serialEM number flag (which is added sequentially) agaist these 9 list. Finally. I will access the system via
### subprocess method to run the linux cmd mv X Y
list_0 = [ i for i in range(0,100, 9) ]
list_1 = [ i+1 for i in range(0,100, 9) ]
list_2 = [ i+2 for i in range(0,100, 9) ]
list_3 = [ i+3 for i in range(0,100, 9) ]
list_4 = [ i+4 for i in range(0,100, 9) ]
list_5 = [ i+5 for i in range(0,100, 9) ]
list_6 = [ i+6 for i in range(0,100, 9) ]
list_7 = [ i+7 for i in range(0,100, 9) ]
list_8 = [ i+8 for i in range(0,100, 9) ]

for i in tiflist:
	if number_split(i) in list_0:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g0.tif"])
		#print(f"mv {i} {current[-2]}_g0.tif")
	elif number_split(i) in list_1:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g1.tif"])
		#print(f"mv {i} {current[-2]}_g1.tif")
	elif number_split(i) in list_2:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g2.tif"])
		#print(f"mv {i} {current[-2]}_g2.tif")
	elif number_split(i) in list_3:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g3.tif"])
		#print(f"mv {i} {current[-2]}_g3.tif")
	elif number_split(i) in list_4:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g4.tif"])
		#print(f"mv {i} {current[-2]}_g4.tif")
	elif number_split(i) in list_5:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g5.tif"])
		#print(f"mv {i} {current[-2]}_g5.tif")
	elif number_split(i) in list_6:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g6.tif"])
		#print(f"mv {i} {current[-2]}_g6.tif")
	elif number_split(i) in list_7:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g7.tif"])
		#print(f"mv {i} {current[-2]}_g7.tif")
	elif number_split(i) in list_8:
		current = i.split(".")
		subprocess.run(["mv", f"{i}", f"{current[-2]}_g8.tif"])
		#print(f"mv {i} {current[-2]}_g8.tif")
