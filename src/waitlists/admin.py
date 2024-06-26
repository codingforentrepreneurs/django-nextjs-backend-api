from django.contrib import admin

# Register your models here.
from .models import WaitlistEntry

admin.site.register(WaitlistEntry)