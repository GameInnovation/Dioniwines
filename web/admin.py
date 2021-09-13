from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from .models import Image, CityDetail, Feeddback, Order

# Register your models here.


# class ImageAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', )


class OrderResized(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


class FeddbackAdmin(admin.ModelAdmin):
  readonly_fields = ('created',)


class OrderkAdmin(admin.ModelAdmin):
  readonly_fields = ('placed',)

admin.site.register(Image)
# admin.site.register(Citie)
admin.site.register(CityDetail)
admin.site.register(Feeddback, FeddbackAdmin)
admin.site.register(Order, OrderResized)
