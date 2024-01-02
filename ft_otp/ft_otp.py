import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", dest="hexa_key", help="""Generate an encrypted key in key.hex from a
					hexadecimal of at least 64 characters""")
parser.add_argument("-k", dest="key", help=""""Generate a TOTP using the encrypted key""")
args = parser.parse_args()

#-------------------------------------------------------------------------------------------------#

	