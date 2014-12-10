from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode
import time, os, operator, sys
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import News_Other


#d = feedparser.parse('http://mmjbusinessdaily.com/feed/')
#d = feedparser.parse('http://feeds.sciencedaily.com/sciencedaily/mind_brain/marijuana')
#d = feedparser.parse('http://www.420magazine.com/forums/external.php?type=rss&forumids=369')
d = feedparser.parse('http://www.thedailychronic.net/feed/')

listx = [ ]

try:
	count = 0
	while count < 10:
		d = feedparser.parse('http://www.thedailychronic.net/feed/')
		title = d['entries'][count]['title']
		link_long = d['entries'][count]['link']
		shortener = Shortener('GoogleShortener')
		link = shortener.short(link_long)
		published_long = d['entries'][count]['published']
		r = published_long.split()
		del r[0]
		del r[3:]
		l = " ".join(str(i) for i in r)
		published = datetime.strptime(l,'%d %b %Y')
		summary = d['entries'][count]['summary'][0:290] + "..."
		count += 1
		print count
		q = News_Other(title=title, link=link, published=published, summary=summary)
		q.save()
except:
	pass
	