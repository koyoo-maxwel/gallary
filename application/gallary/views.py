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
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallary/search.html',{"message":message,"images":searched_images})

    else:
        message = "Sorry! couldn't find that image"

        return render(request, 'all-gallary/search.html',{"message":message})



def image(request,image_id):
        image = Image.objects.get_image_by_id(id = image_id)
        return 'image'