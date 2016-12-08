from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import employee
from .forms import addEmployee
from contact.models import contact


@user_passes_test(lambda u: u.is_superuser)
def manager(request):
    template = loader.get_template('manager.html')
    form = addEmployee(request.POST)
    all_employees = employee.objects.all()
    read_messages = contact.objects.all()
    unread_messages = contact.objects.filter(read="False")
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


def employeeDetail(request, employee_id):
    return HttpResponse(str(employee_id))
