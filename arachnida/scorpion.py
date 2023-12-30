import argparse
import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS


parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs="+", help="Files to parse")
arg = parser.parse_args()

def	display_path_to_file(path: str):
	print("PATH to file: ", path)

def	display_creation_date(path: str):
	c_timestamp = os.path.getctime(path)
	c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)
	print('CREATION DATE/TIME:', c_datestamp)

def	display_EXIF_data(path: str):
	image = Image.open(path)

	info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
	}

	for label,value in info_dict.items():
		print(f"{label:25}: {value}")

	# for tag_id in exif_data:
	# 	print("In loop")
	# 	# get the tag name, instead of human unreadable tag id
	# 	tag = TAGS.get(tag_id, tag_id)
	# 	data = exif_data.get(tag_id)
	# 	# decode bytes 
	# 	if isinstance(data, bytes):
	# 		data = data.decode()
	# 	print(f"{tag:25}: {data}")


for file in arg.files:
	display_path_to_file(file)
	display_creation_date(file)
	display_EXIF_data(file)
	print("\n -------------------------------- \n")
