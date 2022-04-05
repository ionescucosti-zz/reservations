from django.contrib import admin
from scheduler.models import Reservations, Rental

admin.site.register(Rental)
admin.site.register(Reservations)
