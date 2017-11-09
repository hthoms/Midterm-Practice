import 
import urllib.request, urllib.parse, urllib.error

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

while True:
	loc = input("Enter a place")
	if len(loc) < 1:
		break
	#makes url the base url + location
	url = serviceurl+urllib.parse.urlencode({'address':'address'})
	print("Retrieving", url)
	#opens url
	uh = urllib.request.urlopen(url)
	#
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None
		