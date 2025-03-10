from django.contrib import admin

from .models import Discount, Item, Tax, Order


admin.site.register(Discount)
admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Order)
