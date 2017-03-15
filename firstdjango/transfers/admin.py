from django.contrib import admin



# Register your models here.
from .models import Hotels, Transfers

class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','latt','long']
class TransfersAdmin(admin.ModelAdmin):
	list_display = ['from_loc','to_loc','item']

admin.site.register(Transfers,TransfersAdmin)