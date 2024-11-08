from django.contrib import admin
from .models import Predmet,Category
# Register your models here.
admin.site.register([Category ])

@admin.register(Predmet)
class PredmetAdmin(admin.ModelAdmin):
    list_filter = ['category']
    list_display = ['name', 'price','description']
    
    list_display = ['name']