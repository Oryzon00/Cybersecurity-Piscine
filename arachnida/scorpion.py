# The second scorpion program receive image files as parameters and must be able to
# parse them for EXIF and other metadata, displaying them on the screen.

# The program must at least be compatible with the same extensions that spider handles.

# It display basic attributes such as the creation date, as well as EXIF data. The output format is up to you.
# ./scorpion FILE1 [FILE2 ...]

# parse args

# display name of file

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", help="Files to parse")
arg = parser.parse_args()

for file in arg.files:
	print("FILENAME: " + file)
	print("\n -------------------------------- \n")
