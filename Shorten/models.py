from django.db import models

# Create your models here.
class Shorten(models.Model):
    link = models.CharField(max_length=10,unique=True)
    original = models.URLField(max_length=2083)
    def __str__(self):
        return f"{self.original}"
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-created_on",)
class Tracker(models.Model):
    shorten = models.OneToOneField(Shorten,on_delete=models.CASCADE,related_name="shorten_tracker")
    tracker = models.CharField(max_length=12,unique=True)
class Log(models.Model):
    tracker=models.ForeignKey(Tracker,on_delete=models.CASCADE,related_name="shorten_log")
    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=1000) 
    device = models.CharField(max_length=20)
    logged_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-logged_on",)