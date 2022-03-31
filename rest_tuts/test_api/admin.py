from django.contrib import admin
from .models import Shows, Booked, movie


admin.site.register(Shows)
admin.site.register(Booked)
admin.site.register(movie)
