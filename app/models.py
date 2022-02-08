from unicodedata import name
from django.db import models

# Create your models here.
class CONTACT_MODAL(models.Model):
    name = models.CharField(max_length=100, default='Unknown Name')
    email = models.CharField(max_length=100, default='Unknown Email')
    msg = models.CharField(max_length=100, default='Unknown Msg')