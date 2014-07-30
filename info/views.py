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
    return True