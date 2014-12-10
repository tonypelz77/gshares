from django.conf.urls import patterns, url
from gshares import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name = 'index'),
	url(r'^about', views.about, name = 'about'),
	url(r'^forums', views.forums, name = 'forums'),
	url(r'^contact', views.contact, name = 'contact'),
	url(r'^advertise', views.advertise, name = 'advertise'),
	url(r'^charts', views.charts, name = 'charts'),
	#url(r'^stocks', views.stocks, name = 'stocks'),
	url(r'^news', views.news, name = 'news'),
	url(r'^chat', views.chat, name = 'chat'),
	url(r'^privacy', views.privacy, name = 'privacy'),
	url(r'^disclaimer', views.disclaimer, name = 'disclaimer'),
	url(r'^terms', views.terms, name = 'terms'),
	url(r'^twitter', views.twitter, name = 'twitter'),
	url(r'^industry', views.industry, name = 'industry'),
	url(r'^overview', views.overview, name = 'overview'),
	url(r'^AERO', views.AERO, name = 'AERO'),
	url(r'^IMLFF', views.IMLFF, name = 'IMLFF'),
	url(r'^AGTK', views.AGTK, name = 'AGTK'),
	url(r'^ATTBF', views.ATTBF, name = 'ATTBF'),
	url(r'^CBIS', views.CBIS, name = 'CBIS'),
	url(r'^CGRW', views.CGRW, name = 'CGRW'),
	url(r'^EDXC', views.EDXC, name = 'EDXC'),
	url(r'^ENRT', views.ENRT, name = 'ENRT'),
	url(r'^ERBB', views.ERBB, name = 'ERBB'),
	url(r'^FITX', views.FITX, name = 'FITX'),
	url(r'^GBLX', views.GBLX, name = 'GLBX'),
	url(r'^GRCU', views.GRCU, name = 'GRCU'),
	url(r'^GRNH', views.GRNH, name = 'GRNH'),
	url(r'^HEMP', views.HEMP, name = 'HEMP'),
	url(r'^MCIG', views.MCIG, name = 'MCIG'),
	url(r'^MDBX', views.MDBX, name = 'MDBX'),
	url(r'^MJMJ', views.MJMJ, name = 'MJMJ'),
	url(r'^MJNA', views.MJNA, name = 'MJNA'),
	url(r'^MJNE', views.MJNE, name = 'MJNE'),
	url(r'^MNTR', views.MNTR, name = 'MNTR'),
	url(r'^MYEC', views.MYEC, name = 'MYEC'),
	url(r'^NVLX', views.NVLX, name = 'NVLX'),
	url(r'^PHOT', views.PHOT, name = 'PHOT'),
	url(r'^PMCM', views.PMCM, name = 'PMCM'),
	url(r'^QEDN', views.QEDN, name = 'QEDN'),
	url(r'^RSSFF', views.RSSFF, name = 'RSSFF'),
	url(r'^SPRWF', views.SPRWF, name = 'SPRWF'),
	url(r'^SRNA', views.SRNA, name = 'SRNA'),
	url(r'^STEV', views.STEV, name = 'STEV'),
	url(r'^TAUG', views.TAUG, name = 'TAUG'),
	url(r'^THCZ', views.THCZ, name = 'THCZ'),
	url(r'^TRTC', views.TRTC, name = 'TRTC'),
	url(r'^TURV', views.TURV, name = 'TURV'),
	url(r'^UPOT', views.UPOT, name = 'UPOT'),
	url(r'^VAPO', views.VAPO, name = 'VAPO'),
	url(r'^VPOR', views.VPOR, name = 'VPOR'),
	url(r'^AVTC', views.AVTC, name = 'AVTC'),
	url(r'^BRDT', views.BRDT, name = 'BRDT'),
	url(r'^CANL', views.CANL, name = 'CANL'),
	url(r'^CANV', views.CANV, name = 'CANV'),
	url(r'^CBDS', views.CBDS, name = 'CBDS'),
	url(r'^CBGI', views.CBGI, name = 'CBGI'),
	url(r'^CHUM', views.CHUM, name = 'CHUM'),
	url(r'^CNBX', views.CNBX, name = 'CNBX'),
	url(r'^EAPH', views.EAPH, name = 'EAPH'),
	url(r'^ENDO', views.ENDO, name = 'ENDO'),
	url(r'^FULL', views.FULL, name = 'FULL'),
	url(r'^FWDG', views.FWDG, name = 'FWDG'),
	url(r'^GWPH', views.GWPH, name = 'GWPH'),
	url(r'^HMKTF', views.HMKTF, name = 'HMKTF'),
	url(r'^ICBU', views.ICBU, name = 'ICBU'),
	url(r'^LGBI', views.LGBI, name = 'LGBI'),
	url(r'^LVVV', views.LVVV, name = 'LVVV'),
	url(r'^MDCN', views.MDCN, name = 'MDCN'),
	url(r'^NDEV', views.NDEV, name = 'NDEV'),
	url(r'^NTRR', views.NTRR, name = 'NTRR'),
	url(r'^PLPL', views.PLPL, name = 'PLPL'),
	url(r'^REFG', views.REFG, name = 'REFG'),
	url(r'^SING', views.SING, name = 'SING'),
	url(r'^VAPE', views.VAPE, name = 'VAPE'),
	)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	