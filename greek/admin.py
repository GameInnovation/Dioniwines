from django.contrib import admin
from .models import CityDetail

# Register your models here.


# class ImageAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', )


# class FeddbackAdmin(admin.ModelAdmin):
#   readonly_fields = ('created',)


# admin.site.register(Image)
# admin.site.register(Citie)
admin.site.register(CityDetail)
# admin.site.register(Feeddback, FeddbackAdmin)
