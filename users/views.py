from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import User
from django.template import RequestContext, loader


def index(request):
    users = User.objects.all()
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {
        'users': users,
    })
    return HttpResponse(template.render(context))