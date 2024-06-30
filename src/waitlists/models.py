from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL # "auth.User" 

# Create your models here.
class WaitlistEntry(models.Model):
    # user = 
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    # user_id ^
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)