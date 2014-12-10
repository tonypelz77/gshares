from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader, Template
from urllib2 import Request, urlopen
from urllib import urlencode
import time, os, operator, datetime
import feedparser
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import News_Other, Financial, News_Summary, News_Co
import django
django.setup()

def index(request):

	context_listr = [ ]
	listr = Financial.objects.all()
	
	for r in listr:	   
		a = r.ticker
		b = r.name
		c = r.mktcap
		d = r.wkH
		e = r.wkL
		f = r.price
		message = a, b, c, d, e, f
		context_listr.append(message)
	
	sorted_xr = sorted(context_listr, key=lambda x: x[2], reverse=True)
	sorted_xrz = sorted_xr[0:25]
	
	context_listz = [ ]
	listz = News_Other.objects.all()
	
	for z in listz:	   
		a = z.title
		b = z.link
		c = z.published
		d = z.summary
		message = a, b, c, d
		context_listz.append(message)
	
	sorted_xz = sorted(context_listz, key=lambda x: x[2], reverse=True)
	sorted_xyz = sorted_xz[0:2]
	
	t = datetime.now().strftime("%B %d, %Y")
	
	context_list = [ ]
	listx = News_Summary.objects.all()
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		d = x.summary
		
		message = a, b, c, d
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	sorted_xy = sorted_x[0:10]
	return render_to_response('gshares/index.html', {"lists": sorted_xy, "time": t,"listz": sorted_xyz,"listr": sorted_xrz})

def about(request):
			
	context = RequestContext(request)
	context_dict = {'u': "About"}
	return render_to_response('gshares/about.html', context_dict, context)

def contact(request):
			
	context = RequestContext(request)
	context_dict = {'u': "Contact"}
	return render_to_response('gshares/contact.html', context_dict, context)


def news(request):
	
	t = datetime.now().strftime("%B %d, %Y")
	
	context_list = [ ]
	listx = News_Summary.objects.all()
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		d = x.summary
		
		message = a, b, c, d
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	return render_to_response('gshares/news.html', {"lists": sorted_x, "time": t})

def advertise(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Advertise"}
	return render_to_response('gshares/advertise.html', context_dict, context)
	
def charts(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Charts"}
	return render_to_response('gshares/charts.html', context_dict, context)

def forums(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"News"}
	return render_to_response('gshares/forums.html', context_dict, context)
	
def chat(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Chat"}
	return render_to_response('gshares/chat.html', context_dict, context)
	
def privacy(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Privacy"}
	return render_to_response('gshares/privacy.html', context_dict, context)
	
def disclaimer(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Disclaimer"}
	return render_to_response('gshares/disclaimer.html', context_dict, context)
	
def terms(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Terms"}
	return render_to_response('gshares/terms.html', context_dict, context)
	
def twitter(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Twitter"}
	return render_to_response('gshares/twitter.html', context_dict, context)
	
def overview(request):
	
	t = datetime.now().strftime("%B %d, %Y")
	
	context_listn = [ ]
	listn = News_Summary.objects.all()
	
	for x in listn:	   
		a = x.title
		b = x.link
		c = x.date
		d = x.summary
		
		message = a, b, c, d
		context_listn.append(message)
	
	sorted_xn = sorted(context_listn, key=lambda x: x[2], reverse=True)
	sorted_xy = sorted_xn[0:10]
	
	context_list = [ ]
	listx = Financial.objects.all()
	
	for x in listx:	   
		a = x.ticker
		b = x.name
		c = x.mktcap
		d = x.wkH
		e = x.wkL
		f = x.price
		message = a, b, c, d, e, f
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	return render_to_response('gshares/overview.html', {"lists": sorted_x,"time": t,"listn": sorted_xy})
	
def industry(request):

	t = datetime.now().strftime("%B %d, %Y")

	context_list = [ ]
	listx = News_Other.objects.all()
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.published
		d = x.summary
		message = a, b, c, d
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	return render_to_response('gshares/industry.html', {"lists": sorted_x,"time": t})
	context = RequestContext(request)
	
def AERO(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="AERO")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="AERO")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/AERO.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def IMLFF(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="IMLFF")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="IMLFF")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/IMLFF.html', {'name': name, 'ticker': ticker,'lists': sorted_x})

def AGTK(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="AGTK")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="AGTK")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/AGTK.html', {'name': name, 'ticker': ticker,'lists': sorted_x})

def ATTBF(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="ATTBF")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="ATTBF")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/ATTBF.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CBIS(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CBIS")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CBIS")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CBIS.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CGRW(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CGRW")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="CGRW") **DB FIX**
	name = "CannaGrow"
	ticker = "CGRW"
	
	
	return render_to_response('gshares/CGRW.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def EDXC(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="EDXC")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="EDXC") **DB FIX**
	name = "ENDEXX Corp."
	ticker = "EDXC"
	
	
	return render_to_response('gshares/EDXC.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def ENRT(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="ENRT")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="ENRT")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/ENRT.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def ERBB(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="ERBB")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="ERBB")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/ERBB.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def FITX(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="FITX")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="FITX")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/FITX.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def GBLX(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="GBLX")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="GBLX")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/GBLX.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def GRCU(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="GRCU")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="GRCU")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/GRCU.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def GRNH(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="GRNH")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="GRNH")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/GRNH.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def HEMP(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="HEMP")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="HEMP")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/HEMP.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MCIG(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MCIG")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MCIG")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MCIG.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MDBX(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MDBX")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MDBX")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MDBX.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MJMJ(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MJMJ")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MJMJ")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MJMJ.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MJNA(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MJNA")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MJNA")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MJNA.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MJNE(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MJNE")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MJNE")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MJNE.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MNTR(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MNTR")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MNTR")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MNTR.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MYEC(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MYEC")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MYEC")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MYEC.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def NVLX(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="NVLX")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="NVLX")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/NVLX.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def PHOT(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="PHOT")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="PHOT")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/PHOT.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def PMCM(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="PMCM")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="PMCM")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/PMCM.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def QEDN(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="QEDN")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="QEDN")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/QEDN.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def RSSFF(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="RSSFF")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="RSSFF")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/RSSFF.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def SPRWF(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="SPRWF")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="SPRWF")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/SPRWF.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def SRNA(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="SRNA")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="SRNA")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/SRNA.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def STEV(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="STEV")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="STEV")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/STEV.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def TAUG(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="TAUG")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="TAUG")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/TAUG.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def THCZ(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="THCZ")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="THCZ")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/THCZ.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def TRTC(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="TRTC")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="TRTC")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/TRTC.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def TURV(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="TURV")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="TURV")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/TURV.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def UPOT(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="UPOT")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="UPOT")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/UPOT.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def VAPO(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="VAPO")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="VAPO")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/VAPO.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def VPOR(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="VPOR")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="VPOR")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/VPOR.html', {'name': name, 'ticker': ticker,'lists': sorted_x})


'''	
def VAPO(request): #used News db/model
	
	try:
		a = News.objects.get(symbol="VAPO0")
		title_a = a.title
		link_a = a.link
		date_a = a.date
	except:
		title_a = 0
		link_a = 0
		date_a = 0
		
	try:
		b = News.objects.get(symbol="VAPO1")
		title_b = b.title
		link_b = b.link
		date_b = b.date
	except:
		title_b = 0
		link_b = 0
		date_b = 0
		
	try:
		c = News.objects.get(symbol="VAPO2")
		title_c = c.title
		link_c = c.link
		date_c = c.date
	except:
		title_c = 0
		link_c = 0
		date_c = 0
		
	try:		
		d = News.objects.get(symbol="VAPO3")
		title_d = d.title
		link_d = d.link
		date_d = d.date
	
	except:
		title_d = 0
		link_d = 0
		date_d = 0
		
	try:	
		e = News.objects.get(symbol="VAPO4")
		title_e = e.title
		link_e = e.link
		date_e = e.date	
	except:
		title_e = 0
		link_e = 0
		date_e = 0
	
	x = Stock.objects.get(ticker="VAPO")
	name = x.name
	ticker = x.ticker
	
	context = RequestContext(request)
	context_dict = {'name': name, 'ticker': ticker,
					'title_a': title_a,'link_a': link_a, 'date_a': date_a,
					'title_b': title_b,'link_b': link_b, 'date_b': date_b,
					'title_c': title_c,'link_c': link_c, 'date_c': date_c,
					'title_d': title_d,'link_d': link_d, 'date_d': date_d,
					'title_e': title_e,'link_e': link_e, 'date_e': date_e}
	return render_to_response('gshares/VAPO.html', context_dict, context)
'''	
'''
	symbols = ["AERO","AGTK","ATTBF","CBIS","CGRW","EDXC","ENRT","ERBB","FITX","FULL","GBLX",
			   "GRCU","GRNH","HEMP","IMLFF","MCIG","MDBX","MJMJ","MJNA","MJNE","MNTR","MYEC",
			   "NVLX","PHOT","PMCM","QEDN","RSSFF","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC"
			   "TURV","UPOT","VAPO","VPOR"]
	context_dict = { }

	for s in symbols:
		try:
			url = 'http://finance.yahoo.com/rss/headline?s=%s' % s
			shortener = Shortener('GoogleShortener')
			d = feedparser.parse(url)
			v = d.entries[0].link
			y = d.entries[0].title
			p = d.entries[0].published
			r = p.split()
			del r[0]
			del r[3:]
			l = " ".join(str(i) for i in r)
			d = datetime.strptime(l,'%d %b %Y')
			d_now = datetime.now()
			d_max = d_now - timedelta(days=10)
			if d_max > d:
				symbols.remove(s)
				pass
			else:
				x = shortener.short(v)
				message = y, x, p
				context_dict[s] = message
				symbols.remove(s)
		except:
			pass
	
	context = RequestContext(request)
	context_dict = {'s':context_dict}
	return render_to_response('gshares/news.html', context_dict, context)
'''

def AVTC(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="AVTC")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="AVTC")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/AVTC.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def BRDT(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="BRDT")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="BRDT")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/BRDT.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CANL(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CANL")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CANL")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CANL.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CANV(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CANV")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CANV")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CANV.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CBDS(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CBDS")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CBDS")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CBDS.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CBGI(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CBGI")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CBGI")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CBGI.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CHUM(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CHUM")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CHUM")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CHUM.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def CNBX(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="CNBX")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="CNBX")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/CNBX.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def EAPH(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="EAPH")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="EAPH")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/EAPH.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def ENDO(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="ENDO")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="ENDO")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/ENDO.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def FULL(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="FULL")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="FULL") **DB FIX**
	name = "Full Circle Capital"
	ticker = "FULL"
	
	
	return render_to_response('gshares/FULL.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def FWDG(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="FWDG")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="FWDG")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/FWDG.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def GWPH(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="GWPH")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="GWPH") **DB FIX**
	name = "GW Pharm."
	ticker = "GWPH"
	
	
	return render_to_response('gshares/GWPH.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def HMKTF(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="HMKTF")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="HMKTF")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/HMKTF.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def ICBU(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="ICBU")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="ICBU") **DB FIX**
	name = "IMD Companies"
	ticker = "ICBU"
	
	
	return render_to_response('gshares/ICBU.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def LGBI(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="LGBI")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="LGBI") **DB FIX**
	name = "Cannabiz Mobile"
	ticker = "LGBI"
	
	
	return render_to_response('gshares/LGBI.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def LVVV(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="LVVV")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="LVVV")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/LVVV.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def MDCN(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="MDCN")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="MDCN")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/MDCN.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def NDEV(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="NDEV")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="NDEV") **DB FIX**
	name = "Novus"
	ticker = "NDEV"
	
	
	return render_to_response('gshares/NDEV.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def NTRR(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="NTRR")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="NTRR")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/NTRR.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def PLPL(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="PLPL")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="PLPL")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/PLPL.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def REFG(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="REFG")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="REFG") **DB FIX**
	name = "Medical Cannabis"
	ticker = "REFG"
	
	
	return render_to_response('gshares/REFG.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def SING(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="SING")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	#x = Financial.objects.get(ticker="SING") ***Fix for db
	name = "SinglePoint, Inc." 
	ticker = "SING"
	
	
	return render_to_response('gshares/SING.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	
def VAPE(request):
	
	context_list = [ ]
	listx = News_Co.objects.filter(symbol="VAPE")
	
	for x in listx:	   
		a = x.title
		b = x.link
		c = x.date
		
		message = a, b, c
		context_list.append(message)
	
	sorted_x = sorted(context_list, key=lambda x: x[2], reverse=True)
	
	x = Financial.objects.get(ticker="VAPE")
	name = x.name
	ticker = x.ticker
	
	
	return render_to_response('gshares/VAPE.html', {'name': name, 'ticker': ticker,'lists': sorted_x})
	



	
	
	
	
	
	
	













































