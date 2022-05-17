from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models import Avg

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    minimum_age_appropriate = models.IntegerField(default=0, blank=False)
    maximum_age_appropriate = models.IntegerField(default=-1, blank=False)
    def avg_rating(self):
      stars = self.review_set.aggregate(Avg('stars'))
      print(stars)
      return stars['stars__avg']
     
      
    def __str__(self):
        return f"Product {self.name}, price {self.price:.02f}"

class Review(models.Model):
  stars = models.IntegerField(max_length=2, blank=False)
  review = models.CharField(max_length=100,blank=False)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(auth_models.User, models.CASCADE)
  
  def __str__(self):
    return f"Review for {self.product}, {self.stars} stars"

  
  def age_range(self):
      if self.maximum_age_appropriate == -1:
          return f"Ages {self.minimum_age_appropriate} and up"
      elif self.maximum_age_appropriate == self.minimum_age_appropriate:
          return f"Age {self.minimum_age_appropriate}"
      else:
          return f"Ages {self.minimum_age_appropriate} to {self.maximum_age_appropriate}"

