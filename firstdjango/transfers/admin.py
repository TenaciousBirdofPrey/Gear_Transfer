from django.contrib import admin
from .models import Transfers, Hotels

class HotelsAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'hotel_num','hotel_address','latt','long')
    search_fields = ('hotel_name', 'hotel_num')

class TransfersAdmin(admin.ModelAdmin):
    list_display = ('from_loc', 'to_loc','item','drop_date','pick_date')
    search_fields = ('drop_date', 'pick_date','from_loc', 'to_loc')
    list_filter = ('drop_date', 'pick_date','from_loc','to_loc',)
    ordering = ('-drop_date', '-pick_date','-from_loc', '-to_loc',)

admin.site.register(Transfers,TransfersAdmin)
admin.site.register(Hotels, HotelsAdmin)


