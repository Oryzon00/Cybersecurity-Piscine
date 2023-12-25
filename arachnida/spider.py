import argparse

extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

parser = argparse.ArgumentParser()

parser.add_argument("-r", action="store_true", help="recursively downloads the images from an URL")
parser.add_argument("-l", type=int, dest="N", nargs="?", default=5, help="indicates the maximum depth level of the recursive download. If not indicated, it will be 5. -r flag is required")
parser.add_argument("-p", type=str, dest="PATH",nargs="?", default="./data/",  help="indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.")
parser.add_argument("URL", help="indicates the URL from where to extract data")
args = parser.parse_args()

if (args.N and not args.r):
	parser.error("-r is required to use -l")

print(args)
