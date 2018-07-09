from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class creditcard(models.Model):
    friendly_name=models.CharField(max_length=128)
    name_on_card=models.CharField(max_length=128)
    expiry_date=models.CharField(max_length=128)
    type=models.CharField(max_length=128)
    cvv=models.CharField(max_length=128)
    card_no=models.CharField(max_length=128)

    def __str__(self):
        return self.name_on_card

    user = models.ForeignKey(User, on_delete=models.CASCADE)
