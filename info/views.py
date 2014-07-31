from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from info.models import User, Event
from django.template import RequestContext, loader


def index(request):
    users = User.objects.all()
    events = Event.objects.all()
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {
        'users': users,
        'events': events,
    })
    return HttpResponse(template.render(context))

def account(request):
    users = User.objects.first()
    events = Event.objects.all()
    template = loader.get_template('users/account.html')
    context = RequestContext(request, {
        'users': users,
        'events': events,
    })
    return HttpResponse(template.render(context))

def attending(request):
    events = Event.objects.all()
    template = loader.get_template('users/attending.html')
    context = RequestContext(request, {
        'events': events,
    })
    return HttpResponse(template.render(context))

def dnd(request):
    events = Event.objects.all()
    template = loader.get_template('users/DND.html')
    context = RequestContext(request, {
        'events': events,
    })
    return HttpResponse(template.render(context))

def contact(request):
    events = Event.objects.all()
    template = loader.get_template('users/contact.html')
    context = RequestContext(request, {
        'events': events,
    })
    return HttpResponse(template.render(context))