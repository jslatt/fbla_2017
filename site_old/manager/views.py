from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import employee
from .forms import addEmployee
from contact.models import contact


@user_passes_test(lambda u: u.is_superuser)
def manager(request):
    template = loader.get_template('manager.html')
    form = addEmployee(request.POST)
    all_employees = employee.objects.all()
    read_messages = contact.objects.all()
    unread_messages = contact.objects.filter(read="True")
    context = {
        'all_employees': all_employees,
        'form': form,
        'read_messages': read_messages,
        'unread_messages': unread_messages,
    }
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager')
        else:
            form = addEmployee()
            context_data = {'form': form}
            return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))


# add security
class employeeDetail(DetailView):
    model = employee
    template_name = "employeeDetail.html"


@user_passes_test(lambda u: u.is_superuser)
def inbox(request):
    template = loader.get_template('managerInbox.html')
    read_messages = contact.objects.filter(read=False)
    unread_messages = contact.objects.filter(read=True)
    context = {
        'read_messages': read_messages,
        'unread_messages': unread_messages,
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(lambda u: u.is_superuser)
def build(request):
    template = loader.get_template('build.html')
    all_employees = employee.objects.all()
    context = {
        'all_employees': all_employees,
    }
    return HttpResponse(template.render(context, request))


# add security
class messageDetail(DetailView):
    model = contact
    template_name = "contactDetail.html"
