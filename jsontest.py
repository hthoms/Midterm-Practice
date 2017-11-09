import json
import urllib.request

url = input("enter url")
text = urllib.request.urlopen(url).read()

info = json.loads(text)
coms = info["comments"]
sum = 0
for item in coms:
    sum += item["count"]
print(sum)