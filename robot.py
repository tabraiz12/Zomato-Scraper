import requests
from BeautifulSoup import BeautifulSoup as bs
import re
import settings



area = "bangalore"
location = "shivaji nagar"

collection = settings.db[area]

url = "http://www.zomato.com/" + area +"/restaurants"
payload = { 'q' : location }
r = requests.get(url,params = payload)
s = bs(r.text)
res = s.findAll('div',{'class':re.compile(r'\bsearch-name\b')})
for w in res:
	hotels = {}
	name = w.find('h3',{'class':re.compile(r'\btop-res-box-name\b')}).a
	address = w.find('span',{'class':re.compile(r'\bsearch-result-address\b')})
	cuisine = w.find('div',{'class':re.compile(r'\bres-snippet-small-cuisine\b')})
	print name.string
	print address['title']
	print cuisine['title']
	# print name['href']
	print "-----------"
	hotels['name'] = name.string
	hotels['address'] = address['title']
	hotels['cuisine'] = cuisine['title']
	collection.insert(hotels)