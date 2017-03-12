from django.contrib import admin



# Register your models here.
from .models import Hotels

class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','latt','long']

admin.site.register(Hotels,HotelAdmin)