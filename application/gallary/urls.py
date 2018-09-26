from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.today_gallary,name='gallaryToday'),
]