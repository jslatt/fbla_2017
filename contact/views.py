from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import contact
from .forms import contactForm


def contactView(request):
    template = loader.get_template('contact.html')
    form = contactForm(request.POST)
    context = {
            'form': form,
    }
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/success')
        else:
            form = contactForm()
            context_data = {'form': form}
            return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))


def contactSuccess(request):
    return render(request, "contactSuccess.html")