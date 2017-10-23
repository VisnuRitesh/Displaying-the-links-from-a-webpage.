import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter the url: ')
html=urllib.request.urlopen(url).read()
clear=BeautifulSoup(html, 'html.parser')

tags=clear('a')
for tag in tags:
    print(tag.get('href', None))
