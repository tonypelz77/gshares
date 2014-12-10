import time, os, operator
import feedparser
from pyshorteners.shorteners import Shortener
from datetime import datetime, date, timedelta
from gshares.models import News_Co

#symbols = ["AERO","AGTK","ATTBF","AVTC","BRDT","CANL","CANV","CBDS","CBGI","CBIS","CGRW","CHUM","CNBX","EAPH","EDXC"]
#symbols = ["ENDO","ENRT","ERBB","FITX","FULL","FWDG","GBLX","GRCU","GRNH","GWPH","HEMP","HMKTF","ICBU","IMLFF","LGBI"]
#symbols = ["LVVV","MCIG","MDBX","MDCN","MJMJ","MJNA","MJNE","MNTR","MYEC","NDEV","NTRR","NVLX","PHOT","PLPL","PMCM"]
symbols = ["QEDN","REFG","RSSFF","SING","SPRWF","SRNA","STEV","TAUG","THCZ","TRTC","TURV","UPOT","VAPO","VPOR","VAPE"]

context_list = [ ]

for s in symbols:
	try:
		
		count = 0
 		while count < 5:
			url = 'http://finance.yahoo.com/rss/headline?s=%s' % s
			shortener = Shortener('GoogleShortener')
			d = feedparser.parse(url)
			v = d.entries[count].link
			x = shortener.short(v)
			y = d.entries[count].title
			p = d.entries[count].published
			r = p.split()
			del r[0]
			del r[3:]
			l = " ".join(str(i) for i in r)
			d = datetime.strptime(l,'%d %b %Y')
			count += 1
			q = News_Co(symbol=s, title=y, link=x, date=d)
			q.save()
			print "saving to db: %s" % s	

	except:
		pass

