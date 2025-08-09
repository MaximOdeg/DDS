from django.contrib import admin

from .models import Category, Status, Subcategory, Transaction, Type

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transaction)
