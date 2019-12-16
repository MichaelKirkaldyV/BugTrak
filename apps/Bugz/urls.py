from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.homepage),
    url(r'^', views.contact),
    url(r'^', views.about),
    url(r'^', views.login),
]