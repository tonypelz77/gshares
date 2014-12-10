from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode
import time, os, operator
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import Financial

#symbols = ["AERO","AGTK","ATTBF","AVTC","BRDT","CANL","CANV","CBDS","CBGI","CBIS","CGRW","CHUM","CNBX","EAPH","EDXC"]
#symbols = ["ENDO","ENRT","ERBB","FITX","FULL","FWDG","GBLX","GRCU","GRNH","GWPH","HEMP","HMKTF","ICBU","IMLFF","LGBI"]
#symbols = ["LVVV","MCIG","MDBX","MDCN","MJMJ","MJNA","MJNE","MNTR","MYEC","NDEV","NTRR","NVLX","PHOT","PLPL","PMCM"]
symbols = ["QEDN","REFG","RSSFF","SING","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC","TURV","UPOT","VAPO","VPOR","VAPE"]

for s in symbols:
	try:		
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "s")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		t = content.strip('"')
		ticker = str(t)
		print ticker
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "n")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		n = content.strip('"')
		name = str(n)
		print name
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "j1")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		j = content.strip('"M')
		mktcap = float(j)
		print mktcap		
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "p")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		p = content.strip('"')
		price = float(p)
		print price
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "k")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		h = content.strip('"')
		wkH = float(h)	
		print wkH	
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "j")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		l = content.strip('"')
		wkL = float(l)	
		print wkL

		a = Financial(ticker=ticker,name=name,mktcap=mktcap,price=price,wkH=wkH,wkL=wkL)
		a.save()
		print "Saved to db: %s" % s
	except:
		print "error"
		pass








'''	
for s in symbols:
	try:
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "s")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		t = content.strip('"')
		ticker = str(t)
		print ticker
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "n")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		n = content.strip('"')
		name = str(n)
		print name
		r = Stock(ticker=ticker, name=name)
		r.save()
		print "%s saved to Stock db" % s
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "j1")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		j = content.strip('"M')
		mktcap = float(j)
		print mktcap	
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "p")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		p = content.strip('"')
		price = float(p)
		print price
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "k")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		h = content.strip('"')
		wkH = float(h)	
		print wkH	
		url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, "j")
		req = Request(url)
		resp = urlopen(req)
		content = resp.read().decode().strip()
		l = content.strip('"')
		wkL = float(l)	
		print wkL	
		a = Financial(mktcap=mktcap, wkH=wkH, wkL=wkL, price=price, stock=r)
		a.save()
		print "%s saved to Financial db" % s
		r = a.stock
	except:
		pass
'''
