from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Pizza', 'Pizza'),
        ('Burger', 'Burger'),
        ('Cold Coffee', 'Cold Coffee'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    item = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order from {self.customer_name}"

