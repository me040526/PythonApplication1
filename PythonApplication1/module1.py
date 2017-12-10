import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   html = html.decode('utf-8')
   f = open('python.htm','w')
   f.write(html)
   f.close()