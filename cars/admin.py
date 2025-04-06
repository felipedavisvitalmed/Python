from django.contrib import admin
from cars.models import Car,Marca

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
        list_display = ('id', 'name')
        search_fields = ('id','name')





class CarAdmin(admin.ModelAdmin):
        list_display = ('model', 'marca','factory_year','model_year','value')
        search_fields = ('model','marca')


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Car, CarAdmin)