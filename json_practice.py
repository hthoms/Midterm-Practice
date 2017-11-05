import json

diction = {"python":[106,206,330], "html":[336,234], "intro":[106,110]}

res=json.dumps(diction)
f = open('newfile.json', 'w')
f.write(res)
f.close()


print("it worked!")