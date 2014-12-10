from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode
import time, os, operator
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import Stock



#symbols = ["AERO","AGTK","ATTBF","AVTC","BRDT","CANL","CANV","CBDS","CBGI","CBIS","CGRW","CHUM","CNBX","EAPH","EDXC"]
#symbols = ["ENDO","ENRT","ERBB","FITX","FULL","FWDG","GBLX","GRCU","GRNH","GWPH","HEMP","HMKTF","ICBU","IMLFF","LGBI"]
#symbols = ["LVVV","MCIG","MDBX","MDCN","MJMJ","MJNA","MJNE","MNTR","MYEC","NDEV","NTRR","NVLX","PHOT","PLPL","PMCM"]
symbols = ["QEDN","REFG","RSSFF","SING","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC","TURV","UPOT","VAPO","VPOR","VAPE"]

context_list = [ ]
	
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
		q = Stock(ticker=ticker, name=name)
		q.save()
	except:
		pass