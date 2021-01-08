from django.contrib import admin
from .models import Tracker,Shorten,Log
# Register your models here.

admin.site.register([Tracker,Shorten,Log])