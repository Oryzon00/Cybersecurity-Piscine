import argparse
import requests
import sys
import os
from lxml import html
from urllib.parse import urlsplit, urlparse



parser = argparse.ArgumentParser()

parser.add_argument("-r", action="store_true",
					help="recursively downloads the images from an URL")
parser.add_argument("-l", type=int, dest="N", nargs="?", default=5,
					help="""indicates the maximum depth level of the recursive download.
					If not indicated, it will be 5. -r flag is required""")
parser.add_argument("-p", type=str, dest="PATH",nargs="?", default="./data/",
					help="""indicates the path where the downloaded files will be saved.
					If not specified, ./data/ will be used.""")
parser.add_argument("URL", help="indicates the URL from where to extract data")

args = parser.parse_args()

if (sys.argv.__contains__("-l") and not sys.argv.__contains__("-r")):
	parser.error("-r is required to use -l")

print("\n")
print(args)
print("\n")

# print("\n----------------------------------------\n")

#-------------------------------------------------------------------------------------------------#

os.makedirs(name=args.PATH, exist_ok=True)

def get_img_url(src: str) -> str:
	parts_url = urlsplit(args.URL)
	#absolute url
	if (urlparse(src).scheme):
		return (src)
	#protocol relative url
	elif (src.startswith("//")):
		return (parts_url.scheme + ":" + src)
	#relative url
	else:
		return (parts_url.scheme + "://" + parts_url.netloc + src)

def download_img(url: str) -> None:
	response_img = requests.get(url)
	filename = os.path.basename(url)
	open(args.PATH + filename, "wb").write(response_img.content)
	print("Downloaded " + filename + "\nfrom " + url + "\n")

def download_all_imgs_from_url(url: str) -> None:
	response_page = requests.get(args.URL)
	tree = html.fromstring(response_page.content)
	imgs = tree.xpath("//img")
	extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

	for img in imgs:
		src = img.get("src")
		for extension in extensions:
			if (src.endswith(extension)):
				img_url = get_img_url(src)
				download_img(img_url)

def	recursive_download(url:str, n: int):
	print("recursive level: " + str(n))
	download_all_imgs_from_url(url)
	if (n <= 0):
		return
	#get new url
	recursive_download(url, n - 1)

if (args.r):
	recursive_download(args.URL, args.N)
else:
	recursive_download(args.URL, 0)
