import re, urllib
try:
    import urllib.request
except E:
    pass
sites="academy.denarycomputing google yahoo cnn".split()
for s in sites:
    print('Searching:',s)
    try:
        req=urllib.request.urlopen('http://www.'+s+'.com')
    except:
        req=urllib.request.urlopen('http://www.'+s+'.com')
    data=req.read()
    title=re.findall(r'<title>+.*</title>+',str(data),re.I)
    for t in title:
        print(t)
