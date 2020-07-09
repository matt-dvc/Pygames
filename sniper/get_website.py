import requests
from lxml import html, etree
from bs4 import BeautifulSoup as soup


#url = input('Enter address:')
url = str('http://wp.pl')

r = requests.get(url)
r = r.content
r = str(r)
r = html.fromstring(r)
#print(etree.tostring(r, encoding='unicode', pretty_print=True))
print(requests.get(url))
