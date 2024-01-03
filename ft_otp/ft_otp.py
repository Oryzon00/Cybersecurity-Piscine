import argparse
import sys
import hmac

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-g", dest="hexa_key", help="""Generate an encrypted key in key.hex from a
					hexadecimal of at least 64 characters""")
group.add_argument("-k", dest="key", help="""Generate a TOTP using the encrypted key""")
args = parser.parse_args()

#-------------------------------------------------------------------------------------------------#

# Generate encrypted key | -g

def	is_hexadecimal(key: str) -> bool:
	try:
		int(key, 16)
		return (True)
	except ValueError:
		return (False)

def	validate_key(key: str)-> bool:
	if (len(key) < 64):
		return (False)
	return (is_hexadecimal(key))

def	generate_encrypted_key(filename: str):
	print("-g: ", filename)
	try:
		with open(filename, 'r') as f:
			key = f.read()
		if (not validate_key(key)):
			print("ft_otp: error: key must be at least 64 hexadecimal characters.")
			return 
		#need to encrypt key 
		with open('ft_otp.key', 'w') as file:
			file.write(key)
	except Exception as e:
		print("Error: ", e)
		sys.exit(1)
	
	
#-------------------------------------------------------------------------------------------------#

# Generate TOTP | -k

def	hotp(key: str, time):
	return

def	generate_TOTP(filename: str):
	print("-k: ", filename)
	try:
		with open(filename, 'r') as file:
			key = file.read()
		print("content: ", key)
	except Exception as e:
		print("Error: ", e)
		sys.exit(1)


#-------------------------------------------------------------------------------------------------#

def	main():
	if (args.hexa_key is not None):
		generate_encrypted_key(args.hexa_key)
	elif (args.key is not None):
		generate_TOTP(args.key)

if __name__ == "__main__":
	main()
