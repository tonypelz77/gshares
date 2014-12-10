from django.db import models

class Financial(models.Model):
	ticker = models.CharField(max_length=6, unique=True)
	name = models.CharField(max_length=50)
	mktcap = models.IntegerField()
	wkH = models.FloatField()
	wkL = models.FloatField()
	price = models.FloatField()
	
	def __unicode__(self):
		return self.ticker
		return self.name
		return self.mktcap
		return self.wkH
		return self.wkL
		return self.price

class News_Other(models.Model):
	title = models.CharField(max_length=150, unique=True)
	link = models.CharField(max_length=50)
	summary = models.CharField(max_length=300)
	published = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title
		return self.link
		return self.summary
		return self.published

class News_Summary(models.Model):
	title = models.CharField(max_length=150, unique=True)
	link = models.CharField(max_length=50)
	date = models.CharField(max_length=50)
	summary = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.title
		return self.link
		return self.date
		return self.summary

class News_Co(models.Model):
	title = models.CharField(max_length=300, unique=True)
	symbol = models.CharField(max_length=6)
	link = models.CharField(max_length=50)
	date = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title
		return self.symbol
		return self.link
		return self.date
