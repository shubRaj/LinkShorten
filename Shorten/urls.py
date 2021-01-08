from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView
app_name="app_shorten"
urlpatterns = [
    re_path("^(?P<tracker>\w{12})$",views.trackerlink,name="trackerurl"),
    re_path("^(?P<shorten>\w{10})$",views.shortenlink,name="shortenurl"),
    path("",views.HomeView.as_view(),name="shorten_home"),
]
