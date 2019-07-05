from django.contrib import admin

from .models import Person, Public


admin.site.register(Person)
admin.site.register(Public)
