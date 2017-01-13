from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^contact/$', views.contactView, name='contact'),
    url(r'^contact/success$', views.contactSuccess, name='contactSuccess'),
]