import argparse
import os
import datetime
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs="+", help="Files to parse")
arg = parser.parse_args()

def	display_creation_date(path: str):
	c_timestamp = os.path.getctime(path)
	c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)
	print('CREATION DATE/TIME:', c_datestamp)

def	display_path_to_file(path: str):
	print("PATH to file: ", path)

for file in arg.files:
	display_path_to_file(file)
	display_creation_date(file)
	print("\n -------------------------------- \n")
