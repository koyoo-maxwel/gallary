from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image

# my views registered here

def today_gallary(request):
    date = dt.date.today()
    gallary = Image.today_gallary()
    return render(request,'all-gallary/today-gallary.html',{'date': date,"gallary":gallary})

