#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request,"about.html")


@login_required(login_url="login/")
def settings(request):
    return render(request,"settings.html")

