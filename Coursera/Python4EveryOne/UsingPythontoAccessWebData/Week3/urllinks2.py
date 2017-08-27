# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

def nextUrl(c, p, u):
    if(c <= 0 ):
        return

    print("Retrieving: " + str(u))
    url = u
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    As = []
    for tag in tags:
        As.append(tag.get('href', None))
    c -= 1
    nextUrl(c, p, As[p])



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = int(input("Count: "))
pos = int(input("Position: "))
pos -= 1

print("Retrieving: " + url)

tags = soup('a')
As = []
for tag in tags:
    As.append(tag.get('href', None))

nextUrl(count, pos, As[pos])
