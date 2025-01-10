from django.db import models

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

    def __str__(self):
        ordering = ['id']  # Default ordering by ID
        # Display name, category, and stock quantity in a readable format
        return f"{self.name} (Category: {self.category}, Stock: {self.stock_quantity})"
    