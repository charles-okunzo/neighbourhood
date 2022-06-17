from django.contrib import admin

from myhood_app.models import Business, Neighbourhood

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)