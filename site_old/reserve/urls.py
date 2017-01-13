from django.conf.urls import url
from . import views


urlpatterns = [
     url(r'^reserve/$', views.reserveView, name='reserve'),
]