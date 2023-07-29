from django.contrib import admin
from .models import *

class ShowRoomAdmin(admin.ModelAdmin):
    list_display=('name','owner','estb')
    list_filter= ('name','owner')

class BrandAdmin(admin.ModelAdmin):
    list_display=('name','estb','owner','contact')
    search_fields= ('name',)


class ModelAdmin(admin.ModelAdmin):
    list_display=('name','generation','brand')
    list_filter= ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display=('model','year','ChasisNo', 'engine')
    search_fields= ('model',)


class EngineModelAdmin(admin.ModelAdmin):
    list_display=('engine','type','manufacturer','year')
    list_filter= ('type','manufacturer')


class EngineAdmin(admin.ModelAdmin):
    list_display=('engineNo','engineModel')
    search_fields= ('engineNo','engineModel')


class FeaturesAdmin(admin.ModelAdmin):
    list_display=('model','seating_Capacity','horsepower','transmission')
    list_filter= ('model','seating_Capacity','horsepower','transmission')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'age', 'gender', 'city')
    list_filter= ('age', 'gender')
    search_fields= ('designation',)


admin.site.register(ShowRoom, ShowRoomAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(EngineModel, EngineModelAdmin)
admin.site.register(Engine,EngineAdmin )
admin.site.register(Features,FeaturesAdmin )
admin.site.register(Staff,StaffAdmin )
