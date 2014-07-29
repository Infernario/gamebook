from django.contrib import admin

# Register your models here.
from django.contrib import admin
from users.models import User
from users.models import Event

admin.site.register(User)
admin.site.register(Event)
