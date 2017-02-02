import urllib, urllib2
from bs4 import BeautifulSoup, Comment
url1='http://newsite.thehindu.com/opinion/editorial/'
content1 = urllib2.urlopen(url1).read()
soup1 = BeautifulSoup(content1, "html.parser")
alledd=soup1.find_all('div',attrs={"class" : "dd-slide"})
#for i in alledd:
#	print i
#print alledd[0]
print len(alledd)
l= alledd[0].find_all('li')
for i in l:
	print i.text
print i
#print len(list(alledd[0]))
url='http://newsite.thehindu.com/opinion/editorial/Theresa-May%E2%80%99s-underwhelming-visit/article16292161.ece'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
rows=soup.find('none')
print rows.text
topic=soup.find('h1',attrs={"class" : "artcl-nm-stky-text"})
print topic.text
for row in soup.find_all('p',attrs={"class" : "drop-caps"}):
	print row.text
f=open('Desktop/editorial.txt','w')
f.write('hello')
f.close()
