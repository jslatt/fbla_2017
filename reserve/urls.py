from django.conf.urls import url
from . import views


urlpatterns = [
     url(r'^packages/$', views.reserveView, name='reserve'),
]
