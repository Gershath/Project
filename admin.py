from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product, CartItem


# Custom admin configuration for the custom user model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']

# Register the custom user and product models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(CartItem)



