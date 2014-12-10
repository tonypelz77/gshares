import time, os, operator
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import News_Summary
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode


#symbols = ["AERO","AGTK","ATTBF","AVTC","BRDT","CANL","CANV","CBDS","CBGI","CBIS","CGRW","CHUM","CNBX","EAPH","EDXC"]
#symbols = ["ENDO","ENRT","ERBB","FITX","FULL","FWDG","GBLX","GRCU","GRNH","GWPH","HEMP","HMKTF","ICBU","IMLFF","LGBI"]
#symbols = ["LVVV","MCIG","MDBX","MDCN","MJMJ","MJNA","MJNE","MNTR","MYEC","NDEV","NTRR","NVLX","PHOT","PLPL","PMCM"]
symbols = ["QEDN","REFG","RSSFF","SING","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC","TURV","UPOT","VAPO","VPOR","VAPE"]

for s in symbols:
	try:
		url = 'http://finance.yahoo.com/rss/headline?s=%s' % s
		shortener = Shortener('GoogleShortener')
		f = feedparser.parse(url)
		link_long = f.entries[0].link
		print link_long
		title = f.entries[0].title
		print title
		summary = f.entries[0].summary[0:270] + "..."
		print summary
		published = f.entries[0].published
		print published
		adj_pub = published.split()
		del adj_pub[0]
		del adj_pub[3:]
		l = " ".join(str(i) for i in adj_pub)
		pub = datetime.strptime(l,'%d %b %Y')
		link = shortener.short(link_long)
		
		q = News_Summary(title=title, link=link, date=pub, summary=summary)
		q.save()
		print "saving to db: %s" % s
		#symbols.remove(s)
	except:
		pass