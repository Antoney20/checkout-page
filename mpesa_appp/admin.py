from django.contrib import admin

#mine
from.models import Registration, Item,RegisterItem,Order,OrderItem

# Register your models here.
admin.site.register(Registration)
admin.site.register(Item)
admin.site.register(RegisterItem)
admin.site.register(Order)
admin.site.register(OrderItem)
