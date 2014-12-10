import time, os, operator
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import News

symbols = ["AERO","AGTK","ATTBF","CBIS","CGRW","EDXC","ENRT","ERBB","FITX","FULL","GBLX","GRCU","GRNH","HEMP","IMLFF","MCIG","MDBX","MJMJ","MJNA","MJNE","MNTR"]
#symbols = ["MYEC","NVLX","PHOT","PMCM","QEDN","RSSFF","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC","TURV","UPOT","VAPO","VPOR"]

context_list = [ ]


for s in symbols:
	try:
		count = 0
 		while count < 5:
			url = 'http://finance.yahoo.com/rss/headline?s=%s' % s
			shortener = Shortener('GoogleShortener')
			d = feedparser.parse(url)
			#print len(d['entries'])
			v = d.entries[count].link
			x = shortener.short(v)
			y = d.entries[count].title
			p = d.entries[count].published
			c = str(count)
			a = s + c
			print a
			#r = p.split()
			#del r[0]
			#del r[3:]
			#l = " ".join(str(i) for i in r)
			#z = datetime.strptime(l,'%d %b %Y')
			#print z
			#d_now = datetime.now()
			#d_max = d_now - timedelta(days=30)
			count += 1
			print count
			print s
			q = News(symbol=a, title=y, link=x, date=p)
			q.save()

	except:
		pass

		
