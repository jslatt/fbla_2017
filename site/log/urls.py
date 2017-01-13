#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^about/', views.about, name='about'),
    url(r'^services/', views.services, name='services'),
]
