
from django.conf.urls import url,include
from texonomy.views import Genre,show_genres

urlpatterns = [
    url(r'^genres/$', show_genres),
   
]
