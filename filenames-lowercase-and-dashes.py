import glob, re, os


for filename in glob.glob('*.xlsx' ):
	new_name = filename.lower()
	new_name = new_name.replace(" ", "-") 
	new_name = new_name.replace("--", "-")
	print(filename, ' -> ', new_name)
	os.rename(filename, new_name)

'''for filename in glob.glob('*.xlsx' ):
	pattern = r'(.*)request-updates.xlsx'
	replace = r'request-updates-\1.xlsx'
	new_name = re.sub(pattern, replace, filename)
	print(filename, ' -> ', new_name)
	os.rename(filename, new_name)'''
