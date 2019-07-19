import requests
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup



base_url = "http://python.org"



def filename_from_url(url):
	filename = url.replace('http://', '').replace('https://', '').replace('www', '').replace('.', '_').replace('/', '__')

	filename = "{}.csv".format(filename)
	return filename


file_name = filename_from_url(base_url)

html = urlopen(base_url)
bsObj = BeautifulSoup(html.read(), features="html.parser")

links_found = []

for link in bsObj.find_all('a'):
	link_found = urljoin(base_url, link.get('href'))
	links_found.append(link_found)


unique_links = set(links_found)

with open(file_name, 'w') as f:
	for l in unique_links:
		f.write("{}\n".format(l))

unique_links_found = len(unique_links)


print("Getting links from:\t{}".format(base_url))
print("Links found: \t\t{}".format(unique_links_found))
print("Saved file: \t\t{}".format(file_name))
