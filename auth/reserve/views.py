from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import reserve
from .forms import reserveForm


def reserveView(request):
    template = loader.get_template('reserve.html')
    form = reserveForm(request.POST)
    context = {
            'form': form,
    }
    if request.method == 'POST':
        form = reserveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/success')
        else:
            form = reserveForm()
            context_data = {'form': form}
            return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))