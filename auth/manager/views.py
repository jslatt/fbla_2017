from .models import employee
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse
from django.template import loader


@user_passes_test(lambda u: u.is_superuser)
def manager(request):
    template = loader.get_template('manager.html')
    all_employees = employee.objects.all()
    context = {
        'all_employees': all_employees,
    }
    return HttpResponse(template.render(context, request))
