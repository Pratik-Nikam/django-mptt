from django.shortcuts import render
from .models import Genre
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accounts/login/')
def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})