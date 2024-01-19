import argparse
import sys
import logging

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

def	reverse_stockholm():
	print("reverse stockholm")
	return 0

def	stockholm():
	print("stockholm")
	return 0

def	main():
	try:
		args = parse_args()
		if (args.version):
			print_version()
		elif(args.reverse):
			reverse_stockholm
		else:
			stockholm()

	except Exception as e:
		logging.error("An error occurred.", exc_info=True)	
		sys.exit(2)
	return 0

if __name__ == "__main__":
	main()
