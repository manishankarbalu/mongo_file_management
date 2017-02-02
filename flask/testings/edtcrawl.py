import urllib, urllib2 ,sys
from bs4 import BeautifulSoup, Comment

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def printedit(url):
	edfile=open('/home/manishankar/Desktop/editorial.txt','a')
	content = urllib2.urlopen(url).read()
	l=[]	
	soup = BeautifulSoup(content, "html.parser")
	rows=soup.find('none')
	edfile.write( rows.text)
	edfile.write('\n')
	topic=soup.find('h1',attrs={"class" : "artcl-nm-stky-text"})
	edfile.write((topic.text).encode("UTF-8"))
	edfile.write('\n')
	for row in soup.find_all('p',attrs={"class" : "drop-caps"}):
		s= row.text
		print type(s)
		sutf = s.encode("UTF-8")
		#print type(stuf8)
		try:
			edfile.write(sutf)
		except:
			print 'exception'
		#print sutf8
                l.append(sutf)
	edfile.write('\n')
	edfile.write('\t\t-------------------------------------\n')
	edfile.close()
	return l


url1='http://newsite.thehindu.com/opinion/editorial/'
content1 = urllib2.urlopen(url1).read()
soup1 = BeautifulSoup(content1, "html.parser")
alledd=soup1.find_all('div',attrs={"class" : "dd-slide"})
t=[]
l=[]
r=len(alledd)
print r
for i in range(0,r):
	t=alledd[i].find_all('li')
	for i in t:
		k=i.find_all('a',)
		for j in k:
			l.append(j.get('href'))
for i in l:
	printedit(i)

#print len(p)
#print p




