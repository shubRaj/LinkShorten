from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
import string
import random
import datetime
import re
from .forms import ShortenForm
from django.contrib import messages
from .models import Tracker,Shorten,Log
# Create your views here.
def find_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
def find_device(ua):
    regex = re.compile(r'\(.*?\)')
    info = regex.findall(ua)[0].strip("()").split(";")
    return info[1]
def generate_shorten_tracker():
    chars = string.ascii_letters+string.digits
    shorten = "".join([random.choice(chars) for _ in range(10)])
    tracker = "".join([random.choice(chars) for _ in range(12)])
    return shorten,tracker
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Shorten/home.html")
    def post(self,request,*args,**kwargs):
        form = ShortenForm(request.POST)
        if form.is_valid():
            shortenObj = form.save(commit=False)
            while True:
                shorten,tracker=generate_shorten_tracker()
                if not(Shorten.objects.filter(link=shorten).exists()) and not(Tracker.objects.filter(tracker=tracker).exists()):
                    break
            shortenObj.link = shorten
            shortenObj.save()
            trackerObj = Tracker.objects.create(shorten=shortenObj,tracker=tracker)
            return render(request,"Shorten/home.html",{"shorten":shorten,"tracker":tracker})
        return render(request,"Shorten/home.html",{"form":form})
def shortenlink(request,shorten):
    shorten = Shorten.objects.filter(link=shorten)
    if shorten.exists():
        shorten = shorten.first()
        user_agent = request.META.get("HTTP_USER_AGENT")
        device = find_device(user_agent)
        Log.objects.create(tracker=shorten.shorten_tracker,ip=find_ip(request),device=device,
        logged_on=datetime.datetime.now().replace(tzinfo=datetime.timezone.utc),browser=user_agent)
        return redirect(shorten.original)
    messages.error(request,"The URL Doesn't Exist.")
    return redirect("app_shorten:shorten_home")
def trackerlink(request,tracker):
    tracker = Tracker.objects.filter(tracker=tracker)
    if tracker.exists():
        device = find_device(request.META.get("HTTP_USER_AGENT"))
        ip = find_ip(request)
        context = {"logs":tracker.first().shorten_log.all(),"device":device,"ip":ip}
        return render(request,"Shorten/tracker.html",context)
    messages.error(request,"The Tracker Doesn't Exist.")
    return redirect("app_shorten:shorten_home")
