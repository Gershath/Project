from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Custom User model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username






# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# CartItem model
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
