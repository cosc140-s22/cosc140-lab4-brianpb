from django.contrib import admin

from .models import Product
admin.site.register(Product)

from .models import Review
admin.site.register(Review)


