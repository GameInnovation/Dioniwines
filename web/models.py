from typing import Counter
# from web.views import feedback
from django.db import models
from .storage import OverwriteStorage
from django.contrib.auth.models import User


# Create your models here.


# def image_path(instance, filename):
#     return os.path.join('images', str(instance.some_identifier), filename)


class Image(models.Model):
    # Το pip install django-cleanup σβήνει την Photo όταν κάνεις delete απο το admin. Τώρα το έχω περασμένο μέσα. Το ΕΒΓΑΛΑ
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        storage=OverwriteStorage(), upload_to='images', null=True)

    def __str__(self):
        return self.title


# class Citie(models.Model):
#   # Το pip install django-cleanup σβήνει την Photo όταν κάνεις delete απο το admin. Τώρα το έχω περασμένο μέσα. Το ΕΒΓΑΛΑ
#   city_name = models.CharField(max_length=100, blank=True)
#   city_photo = models.ImageField(storage=OverwriteStorage(), upload_to='cities', null=True)

#   def __str__(self):
#       return self.city_name


class CityDetail(models.Model):
    # Το pip install django-cleanup σβήνει την Photo όταν κάνεις delete απο το admin. Τώρα το έχω περασμένο μέσα. Το ΕΒΓΑΛΑ.
    city_name = models.CharField(max_length=100, blank=True)
    person_clients = models.CharField(max_length=100, blank=True)
    top_chefs = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    city_photo = models.ImageField(
        storage=OverwriteStorage(), upload_to='cities', null=True)

    def __str__(self):
        return self.city_name + "  " + "Restaurant Details"


class Feeddback(models.Model):
    customer_first_name = models.CharField(max_length=100, blank=True)
    customer_second_name = models.CharField(max_length=100, blank=True)
    feedback_description = models.CharField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True, blank=True)

    datecompleted = models.DateTimeField(null=True, blank=True)
    # Κλειδώνει τον User με το σιγκεκριένο Feedback
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    # Δεν χρειάζεται Migration η κάθε αλλαγή εντός των παραμέτρων. ΔΕΝ βάζω Blank=True γιατί θέλω να αφήνει Feedback Υποχρεωτικά.
    feedback = models.TextField(max_length=1000)
    customer_photo = models.ImageField(storage=OverwriteStorage(), upload_to='customer', null=True, blank=True)
    deleted = models.BooleanField()
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_second_name + " " + self.customer_first_name + ":" + "  " + "Feedback"


class Order(models.Model):
    FRANCE = 'France'
    GERMANY = 'Germany'
    UK = 'Great Britain'
    GREECE = 'Greece'
    COUNTRIES = [(FRANCE, 'France'), (GERMANY, 'Germany'), (UK, 'Great Britain'), (GREECE, 'Greece')]

    country = models.CharField(max_length=20, choices=COUNTRIES, default=GREECE)

    town = models.CharField(max_length=100, blank=True)
    
    address = models.CharField(max_length=100, blank=True)
    postalcode = models.CharField(max_length=10, blank=True)

    customer_first_name = models.CharField(max_length=100, blank=True)
    customer_second_name = models.CharField(max_length=100, blank=True)
    order_description = models.CharField(max_length=100, blank=True)

    placed = models.DateTimeField(auto_now_add=True, blank=True)

    datecompleted = models.DateTimeField(null=True, blank=True)
    # Κλειδώνει τον User με το σιγκεκριένο Feedback
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Δεν χρειάζεται Migration η κάθε αλλαγή εντός των παραμέτρων. ΔΕΝ βάζω Blank=True γιατί θέλω να αφήνει Feedback Υποχρεωτικά.
    order = models.TextField(max_length=1000)
    customer_photo = models.ImageField(
        storage=OverwriteStorage(), upload_to='customer', null=True, blank=True)
    deleted = models.BooleanField()
    # show = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_second_name + " " + self.customer_first_name + ":" + "  " + "Order"


class ListOrNot(models.Model):
    lista = models.BooleanField(default=True)

