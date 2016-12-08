#!python
# log/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manager/$', views.manager, name='manager'),
    url(r'manager/edit/(P<employee_id[0-9]+)/$', views.manager, name='manager'),
]
