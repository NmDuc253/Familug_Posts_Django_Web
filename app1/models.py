from django.db import models

class List_Jobs(models.Model):
	title = models.TextField(unique=True)
	link = models.TextField(unique=True)

	def __str__(self):
		return self.title


class Python(models.Model):
	title = models.TextField(unique=True)
	link = models.TextField(unique=True)

	def __str__(self):
		return self.title


class Command(models.Model):
	title = models.TextField(unique=True)
	link = models.TextField(unique=True)

	def __str__(self):
		return self.title


class Sysadmin(models.Model):
	title = models.TextField(unique=True)
	link = models.TextField(unique=True)

	def __str__(self):
		return self.title


class Latest(models.Model):
	title = models.TextField(unique=True)
	link = models.TextField(unique=True)

	def __str__(self):
		return self.title
	
