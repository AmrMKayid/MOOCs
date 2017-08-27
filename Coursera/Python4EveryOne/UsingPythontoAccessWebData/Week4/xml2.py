import urllib, urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print("Retrieving " + url)
input = urllib.request.urlopen(url).read()
print("Retrieved " + str(len(input)) + " characters")

stuff = ET.fromstring(input)
lst = stuff.findall('.//count')
l = []
for item in lst:
    l.append(item.text)
print(len(l))
print(sum((int(i) for i in l)))
