from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^login$', views.login),
    url(r'^process_inquery$', views.process_inquery),
    url(r'^register$', views.register),
    url(r'^register_process$', views.register_process),
    url(r'^login_process$', views.login_process),
]