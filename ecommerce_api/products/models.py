from django.db import models
from django.core.exceptions import ValidationError

# Model to represent product categories
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique category name

    def __str__(self):
        return self.name  # Display category name in admin and other interfaces

# Model to represent products
class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField()  # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal points
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")  
    # Foreign key linking to Category, with cascade delete
    stock_quantity = models.PositiveIntegerField()  # Number of items in stock (cannot be negative)
    image_url = models.URLField(max_length=500, blank=True, null=True)  # Optional URL for product image
    created_date = models.DateTimeField(auto_now_add=True)

    #validation fields
    def clean(self):
        """Perform custom validations for the product model."""
        if self.price < 0:
            raise ValidationError({'price': "Price cannot be negative."})
        if self.stock_quantity < 0:
            raise ValidationError({'stock_quantity': "Stock quantity cannot be negative."})
        if not self.name.strip():
            raise ValidationError({'name': "Product name cannot be blank or whitespace."})
        if len(self.name) < 3:
            raise ValidationError({'name': "Product name must be at least 3 characters long."})

    def save(self, *args, **kwargs):
        """Validate the product before saving."""
        self.full_clean()  # Ensures the clean method is called
        super().save(*args, **kwargs)

    def __str__(self):
        ordering = ['id']  # Default ordering by ID
        # Display name, category, and stock quantity in a readable format
        return f"{self.name} (Category: {self.category}, Stock: {self.stock_quantity})"
    