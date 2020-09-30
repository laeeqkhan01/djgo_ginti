from django.conf import settings
from django.db   import models

# Create your models here.

class AdadTable(models.Model):
  num = models.IntegerField()
  sqr = models.IntegerField()
  sound = models.CharField(max_length=16)

  def __str__(self):
    return self.sound
  
