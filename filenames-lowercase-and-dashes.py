'simple script for removing spaces, replacing them with dashes, and making a filename all lowercase


import glob, re, os


for filename in glob.glob('*.xlsx' ):
	new_name = filename.lower()
	new_name = new_name.replace(" ", "-") 
	new_name = new_name.replace("--", "-")
	print(filename, ' -> ', new_name)
	os.rename(filename, new_name)


