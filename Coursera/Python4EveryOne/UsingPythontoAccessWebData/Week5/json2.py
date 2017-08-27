import json
import urllib, urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')
print("Retrieving " + url)
data = urllib.request.urlopen(url).read()
print("Retrieved " + str(len(data)) + " characters")

info = json.loads(data)
print('User count:', len(info))

items = info["comments"]

l = []
for item in items:
    l.append(item['count'])

print(len(l))
print(sum((int(i) for i in l)))
