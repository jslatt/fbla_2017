#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="login/")
def settings(request):
    return render(request,"settings.html")

#@user_passes_test(lambda u: u.is_superuser)
#def manager(request):
#    return render(request,"manager.html")
