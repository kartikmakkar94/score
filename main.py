import urllib2
from xml.dom.minidom import parse
import xml.dom.minidom

def main():
	
	webUrl = urllib2.urlopen("http://static.cricinfo.com/rss/livescores.xml")
	code=webUrl.getcode()
	if code>=500:
		print "Server Error"
	data = webUrl.read()
	
	f=open("scores.xml","w+");
	f.write(data);
	f.close();
	
	DOMTree = xml.dom.minidom.parse("scores.xml")
	collection = DOMTree.documentElement
	
	matches=collection.getElementsByTagName("item")

	for match in matches:
		print "Score: %s" %match.getElementsByTagName("description")[0].childNodes[0].data
 
if __name__ == "__main__":
	main()