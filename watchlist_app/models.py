from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class StreamPlateform(models.Model):
  name =models.CharField(max_length=255)
  about = models.CharField(max_length=255)
  website = models.URLField(max_length=255)
  def __str__(self):
    return self.name

class WatchList(models.Model):
  title = models.CharField(max_length=255)
  storyline = models.CharField(max_length=255)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  avg_rating = models.FloatField(default=0.0 ) 
  number_rating = models.IntegerField(default=0)

  plateform = models.ForeignKey(StreamPlateform, on_delete=models.CASCADE, related_name="watchlist")
  def __str__(self):
    return self.title

class Review(models.Model):
  review_user = models.ForeignKey( User, on_delete=models.CASCADE, related_name= 'review_user')
  watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="review")
  rating = models.PositiveIntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)])
  description = models.CharField(max_length=255, null=True)
  active = models.BooleanField(default=True)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self): 
    return str(self.rating) + " - " + self.watchlist.title


# class Movie(models.Model):
#   name = models.CharField(max_length=255)
#   discription = models.CharField(max_length= 255)
#   active = models.BooleanField(default=True)

#   def __str__(self):
#     return self.name
    
