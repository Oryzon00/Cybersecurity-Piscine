import sys
import argparse


extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def program_info():
	print("Here is how you can call this program: ./spider [-rlp] URL\n")
	print("Option -r : recursively downloads the images in a URL")
	print("Option -r -l [N] : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.")
	print("Option -p [PATH] : indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.")

# print("script name:", sys.argv[0])

parser = argparse.ArgumentParser()
# parser.add_argument()
args = parser.parse_args()


# print(args.filename, args.count, args.verbose)

# len = len(sys.argv) - 1

# if (len == 0):
# 	print("wrong number of args")
# 	program_info()
# 	exit


# for i in range(1, len(sys.argv)):
# 	print(sys.argv[i])

# program_info()



# import argparse

# parser = argparse.ArgumentParser(description="My Program")
# parser.add_argument('-r', '--required', help='An optional argument')

# args = parser.parse_args()

# if args.required:
#    print("Optional argument provided:", args.required)
# else:
#    print("No optional argument provided")
