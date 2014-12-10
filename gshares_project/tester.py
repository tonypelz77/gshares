from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode
import time, os, operator, sys
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import Stock, Financial
import django
django.setup()


symbols = "ABIO"
listx = [ ]
		
url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, "n")
req = Request(url)
resp = urlopen(req)
content = resp.read().decode().strip()
n = content.strip('"')
name = str(n)
print name
		
r = Stock(ticker=symbols, name=name)
r.save()

url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, "j1")
req = Request(url)
resp = urlopen(req)
content = resp.read().decode().strip()
j = content.strip('"M')
mktcap = float(j)
print mktcap	
url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, "p")
req = Request(url)
resp = urlopen(req)
content = resp.read().decode().strip()
p = content.strip('"')
price = float(p)
print price
url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, "k")
req = Request(url)
resp = urlopen(req)
content = resp.read().decode().strip()
h = content.strip('"')
wkH = float(h)	
print wkH	
url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbols, "j")
req = Request(url)
resp = urlopen(req)
content = resp.read().decode().strip()
l = content.strip('"')
wkL = float(l)	
print wkL

a = Financial(mktcap=mktcap,wkH=wkH,wkL=wkL,price=price,stock=r)
a.save()

r = a.stock
a = r.name
b = r.ticker

message = a, b, mktcap, price, wkH, wkL
listx.append(message)
print listx







'''
#d = feedparser.parse('http://mmjbusinessdaily.com/feed/')
#d = feedparser.parse('http://feeds.sciencedaily.com/sciencedaily/mind_brain/marijuana')
#d = feedparser.parse('http://www.420magazine.com/forums/external.php?type=rss&forumids=369')
#d = feedparser.parse('http://www.thedailychronic.net/feed/')

listx = [ ]
#len(d['entries'])

#for x in d['entries']:
try:
	count = 0
	while count < 10:
		d = feedparser.parse('http://mmjbusinessdaily.com/feed/')
		title = d['entries'][count]['title']
		link_long = d['entries'][count]['link']
		shortener = Shortener('GoogleShortener')
		link = shortener.short(link_long)
		published = d['entries'][count]['published']
		r = published.split()
		del r[0]
		del r[3:]
		l = " ".join(str(i) for i in r)
		z = datetime.strptime(l,'%d %b %Y')
		print z
		print type(z)
		#summary = d['entries'][count]['summary'][0:150] + "..."
		#article = title, link, published, summary
		#listx.append(article)
		#print "adding article to database"
		count += 1
		print count
except:
	pass
	
print listx[4]
#print d['feed']['title']
#print d.entries[0]
'''