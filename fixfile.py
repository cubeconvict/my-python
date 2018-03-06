import glob, re, os

for allmyfiles in glob.glob(''):
	filename, file_extension = os.path.splitext(allmyfiles)
	if file_extension == '':
		new_name = filename+'.xlsx'
		print(filename, ' -> ', new_name)
		os.rename(filename, new_name)