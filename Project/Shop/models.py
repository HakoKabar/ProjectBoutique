from django.db import models

class Category(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now=True)
     
    name = models.CharField(max_length=50)
    discrapti=models.TextField(blank=True)
    active =models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
class Product(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


