from django.contrib import admin
from .models import CarMake, CarModel

# Register CarMake and CarModel in the admin site
admin.site.register(CarMake)
admin.site.register(CarModel)

