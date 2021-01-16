class RlnToTopaz:
	"""Convert manual/autopick star files from rln to topaz format"""
	"""define arguments required: path to input, path to output"""
	"""asumed file name is a star file from manual/auto pick with image_name_manaulpick.star format"""
	"""extract imagename from file name"""
	def __init__(self, filepath, outputfile=''):
		self.filepath = filepath
		self.outputfile = outputfile
		self.common_header = 'image_name	x_coord	y_coord'
		split_name = self.filepath.split("/")
		self.imgname = split_name[6]
		self.imgname_2 = ''
		if '_manualpick' in self.imgname:
			imgname_split = self.imgname.split("_manual")
			self.imgname_2 = imgname_split[-2]
		elif 'autopick' in self.imgname:
			imgname_split = self.imgname.split("_auto")
			self.imgname_2 = imgname_split[-2]
		header = self.common_header
	def open_and_liner(self):
		"""OPEN FILE AND CREATE A PYTHON FILE OBJECT."""
		"""REMOVE HEADER AND LAST EMPTY LINE"""
		"""LOOP THROUGH EVERY LINE AND SPLIT THEM IN SINGLE-LINE-LISTS"""
		"""OUTPUT POSITION [0] AND [1] FROM EVERY LINE-LIST"""
		"""PRINT FUNCTION OUTPUT IS ALWAYS STR"""
		i_split = []
		var = ''
		with open(self.filepath, 'r') as object_file:
			liner = object_file.readlines()
			liner_2 = liner[11:-1]
			for i in liner_2:
				i_split = i.split()
				var += f"{self.imgname_2} \t{i_split[0]}  \t{i_split[1]}\n"
		#assambled = self.common_header.assambled
		return	var

		#with open(self.outputfile, 'w') as object_file_w:
			#object_file_w.write("testestesttest")