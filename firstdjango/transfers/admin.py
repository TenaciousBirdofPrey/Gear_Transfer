from django.contrib import admin



# Register your models here.
from .models import Hotels, Transfers

class HotelsAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','latt','long']
class TransfersAdmin(admin.ModelAdmin):
	list_display = ['from_loc','to_loc','item']




#admin.site.register(Transfers,TransfersAdmin)
admin.register(Hotels,Transfers)(admin.ModelAdmin)



# # File: admin.py
# from django.contrib import admin
# from .models import Project, Client, About

# admin.register(Project, Client, About)(admin.ModelAdmin)
