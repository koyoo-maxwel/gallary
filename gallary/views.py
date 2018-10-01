from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

from .models import Image,Location,Category

# my views registered here

def today_gallary(request):
    gallary = Image.objects.all()
    return render(request,'all-gallary/today-gallary.html',{"gallary":gallary})


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image_by_name(search_term)
        message = f"{search_term}"
       

        return render(request, 'all-gallary/search.html',{"message":message,"images":searched_images})

    else:
        message = "That was embarrasing! you haven't searched for anything yet."


        return render(request, 'all-gallary/search.html',{"message":message})


def shags(request,location_name):
    image = Location.objects.get(name=location_name)
    image = image.id
    gallary = Image.objects.filter(location_id=image)
    return render(request,'all-gallary/location.html',{'gallary':gallary})
    


def kisumu(request,location_name):
    image = Location.objects.get(name=location_name)
    image = image.id
    gallary = Image.objects.filter(location_id=image)
    return render(request,'all-gallary/location.html',{'gallary':gallary})


def my_best_pics(request,location_name):
    image = Location.objects.get(name=location_name)
    image = image.id
    gallary = Image.objects.filter(location_id=image)
    return render(request,'all-gallary/location.html',{'gallary':gallary})
    

def entertainment(request,location_name):
    image = Location.objects.get(name=location_name)
    image = image.id
    gallary = Image.objects.filter(location_id=image)
    return render(request,'all-gallary/location.html',{'gallary':gallary})
    
    

def travell(request,location_name):
    image = Location.objects.get(name=location_name)
    image = image.id
    gallary = Image.objects.filter(location_id=image)
    return render(request,'all-gallary/location.html',{'gallary':gallary})
    
    






