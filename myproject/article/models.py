from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    shopname = models.CharField(max_length=250)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
