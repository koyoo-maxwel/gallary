from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.today_gallary,name='gallaryToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.Image,name ='image'),
    url(r'^location/(\w+)',views.shags,name='locations'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)