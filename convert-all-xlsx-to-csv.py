import pandas as pd
import glob, re, os


for next_filename in glob.glob('*.xlsx' ):

	read_fileread_file = pd.read_excel (next_filename, sheet_name='Inventory')
	csv_filename = os.path.splitext(next_filename)[0]+".csv"
	read_fileread_file.to_csv (csv_filename, index = None, header=True)