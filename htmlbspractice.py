import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()

print(fhand, type(fhand))
print(html, type(html))
