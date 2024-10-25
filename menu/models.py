from django.db import models




class ProductList(models.Model):

   title = models.CharField(max_length=255)
   description = models.TextField()
   img = models.ImageField(null=True)
   datetime = models.DateField()
   is_active = models.BooleanField(default=True)
