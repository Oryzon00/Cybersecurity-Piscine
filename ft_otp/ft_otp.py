import argparse
import sys
import logging
import hmac
import base64
from cryptography.fernet import Fernet
import time
import pyotp

MASTER_KEY_FILE = ".master.key"

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

def	generate_master_key() -> bytes:
	master_key = Fernet.generate_key()
	with open(MASTER_KEY_FILE, 'wb') as file:
		file.write(master_key)
	return (master_key)

def	read_master_key() -> bytes:
	with open(MASTER_KEY_FILE, "rb") as file:
		master_key = file.read()
	return (master_key)

# get fernet master key from file, generate it if does not exist
def	get_master_key() -> bytes:
	try:
		master_key = read_master_key()
	except FileNotFoundError:
		master_key = generate_master_key()
	return (master_key)

def	encrypt_hexa_key(secret: str) -> bytes:
	master_key = get_master_key()
	f = Fernet(master_key)
	cypher = f.encrypt(secret.encode())
	return (cypher)

def	generate_encrypted_key(filename: str):
		with open(filename, 'r') as f:
			hexa_key = f.read()
		if (not validate_key(hexa_key)):
			print("ft_otp: error: key must be at least 64 hexadecimal characters.")
			return 
		cypher = encrypt_hexa_key(hexa_key)
		with open('ft_otp.key', 'wb') as file:
			file.write(cypher)
			print("Key was successfully saved in ft_otp.key")
	

#-------------------------------------------------------------------------------------------------#

# Generate TOTP | -k

# HOTP
# HMAC-based one-time password

# HMAC
# hash-based message authentication code

def	compute_byte_array(s_bit: bytearray):
	s_num = int(s_bit.hex(), 16)
	return (s_num % 10 ** 6)

def last_31_bits(p):
    res = bytearray()
    res.append(p[0] & 0x7F)    # 7 bits
    for b in p[1:]:
        res.append(b & 0xFF)   # 8 bits
    return res

def	get_low_order_4_bits(value):
	return (value & 0b1111)

def	dynamic_truncation(hashed_secret: bytes):
	offset_bits = get_low_order_4_bits(hashed_secret[19])
	p = hashed_secret[offset_bits:offset_bits+4]
	return (last_31_bits(p))

def	generate_hash_secret(key: str, time_steps: int):
	secret_b = bytes.fromhex(key)
	time_steps_b = time_steps.to_bytes(8, byteorder="big")
	hashed_secret_hmac = hmac.new(secret_b, time_steps_b, "sha1")
	hashed_secret = hashed_secret_hmac.digest()
	return (hashed_secret)

def	hotp(key: str, time_steps: int):
	hashed_secret = generate_hash_secret(key, time_steps)
	s_bits = dynamic_truncation(hashed_secret)
	otp = compute_byte_array(s_bits)
	return otp

def	ft_totp(key: str, time_interval: int):
	second_since_epoch = int(time.time())
	time_steps = int(second_since_epoch / time_interval)
	otp = hotp(key, time_steps)
	return (str(otp).zfill(6))

def	decrypt_key(filename: str):
	with open(filename, 'rb') as file:
		cypher = file.read()
	master_key = read_master_key()
	f = Fernet(master_key)
	secret = f.decrypt(cypher)
	return (secret.decode())

def	generate_TOTP(filename: str):
	time_interval = 30
	key = decrypt_key(filename)
	otp = ft_totp(key, time_interval)
	true_totp = pyotp.TOTP(base64.b32encode(bytes.fromhex(key))).now()
	print(f"{'my otp':20} {otp}")
	print(f"{'true totp':20} {true_totp}")

#-------------------------------------------------------------------------------------------------#

def	main():
	try:
		parser = argparse.ArgumentParser()
		group = parser.add_mutually_exclusive_group(required=True)
		group.add_argument("-g", dest="hexa_key", help="""Generate an encrypted key in key.hex from a
							hexadecimal of at least 64 characters""")
		group.add_argument("-k", dest="key", help="""Generate a TOTP using the encrypted key""")
		args = parser.parse_args()

		if (args.hexa_key):
			generate_encrypted_key(args.hexa_key)
		elif (args.key):
			generate_TOTP(args.key)
	except Exception as e:
		logging.error("An error occurred.", exc_info=True)	
		sys.exit(2)

if __name__ == "__main__":
	main()
