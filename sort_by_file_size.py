import os 
dirpath = '/cryoem-data2/test/small_set'
fileslist = os.listdir(dirpath)
mrclist = []
for i in fileslist:
	if '.mrc' in i:
		mrclist.append(i)
list_imgs_48_frames = []
list_imgs_49_frames = []
for i in range(len(mrclist)):
	i_path = f"{dirpath}/{mrclist[i]}"
	if (os.stat(i_path).st_size) == 4525425664:
		list_imgs_48_frames.append(i_path)
	elif (os.stat(i_path).st_size) == 4619705344:
		list_imgs_49_frames.append(i_path)
list_imgs_48_frames_file = []
for i in list_imgs_48_frames:
	i_split = i.split("/")
	list_imgs_48_frames_file.append(i_split[-1])
list_imgs_49_frames_file = []
for i in list_imgs_49_frames:
	i_split = i.split("/")
	list_imgs_49_frames_file.append(i_split[-1])

to_write_48 = f"{dirpath}/list_files_48_frames.txt"
with open(to_write_48, 'w') as f1:
	for i in list_imgs_48_frames_file:
		f1.write(f"{i}\n")
to_write_49 = f"{dirpath}/list_files_49_frames.txt"
with open(to_write, 'w') as f2:
	for i in list_imgs_49_frames_file:
		f2.write(f"{i}\n")
print(f"Done!")
