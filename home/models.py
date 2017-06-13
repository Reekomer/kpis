from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Stoyo(models.Model):
  datepub = models.DateField(max_length=30)
  page_name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  link = models.CharField(max_length=100,unique=True)
  reactions = models.IntegerField()
  comments = models.IntegerField()
  shares = models.IntegerField()
  views = models.IntegerField()

  def __str__(self):
    return "Stoyo: {}".format(self.link)

#@python_2_unicode_compatible
class Publisher(models.Model):
  datepub = models.DateField(max_length=30, null=True)
  page_name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)  
  link = models.CharField(max_length=100,unique=True)
  reactions = models.IntegerField(null=True)
  comments = models.IntegerField(null=True)
  shares = models.IntegerField(null=True)
  views = models.IntegerField(null=True)