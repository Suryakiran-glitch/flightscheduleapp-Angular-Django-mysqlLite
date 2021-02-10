from django.urls import path
from .views import flight_list , flight_details
from django.conf.urls import url

urlpatterns = [
    url(r'^$', flight_list),
    url(r'^(?P<pk>[0-9]+)$', flight_details)
]