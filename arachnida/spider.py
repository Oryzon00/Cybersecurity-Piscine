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

#-------------------------------------------------------------------------------------------------#

def get_img_url(src: str, url: str) -> str:
	parts_url = urlsplit(url)
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
	print("Downloaded " + filename + "\nFrom " + url + "\n")

def download_all_imgs_from_url(url: str, tree: html.HtmlElement) -> None:
	print("\n----- DOWNLOADING IMAGES FROM : " + url + " -----\n")
	imgs : [html.HtmlElement] = tree.xpath("//img")
	extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

	for img in imgs:
		src = img.get("src")
		if (src is None):
			continue
		for extension in extensions:
			if (src.endswith(extension)):
				img_url = get_img_url(src, url)
				download_img(img_url)

def	get_valid_url_from_href(href: str, url: str, url_list: [str]):
	parts_url = urlsplit(url)
	#Relative url
	if (href.startswith("/")):
		href = parts_url.scheme + "://" + parts_url.netloc + href
		print("Scrapped " + href + "\nFrom " + url + "\n")
		url_list.append(href)
	#Absolute url but same base url
	elif(href.startswith(parts_url.scheme + "://" + parts_url.netloc)):
		url_list.append(href)
	#Invalid href for url
	else:
		return

def	get_url_list_from_anchors(url: str, tree: html.HtmlElement) -> [str]:
	print("\n----- SCRAPPING ALL <a> FROM : " + url + " -----\n")

	url_list = []
	anchors = tree.xpath("//a")
	for anchor in anchors:
		href = anchor.get("href")
		get_valid_url_from_href(href, url, url_list)
	return (url_list)

def	recursive_download(url:str, n: int):
	response_page = requests.get(url)
	tree : html.HtmlElement = html.fromstring(response_page.content)
	download_all_imgs_from_url(url, tree)
	if (n <= 0):
		return
	url_list = get_url_list_from_anchors(url, tree)
	for new_url in url_list:
		recursive_download(new_url, n - 1)

#-------------------------------------------------------------------------------------------------#


if (sys.argv.__contains__("-l") and not sys.argv.__contains__("-r")):
	parser.error("-r is required to use -l")
os.makedirs(name=args.PATH, exist_ok=True)

if (args.r):
	recursive_download(args.URL, args.N)
else:
	recursive_download(args.URL, 0)

print("\n----- DONE -----\n")

#img with same name --> need to change name so i dont write on same file -> default(1), default(2), etc...
