from rest_framework import serializers
from .models import Category, Product

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields of the Category model

# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    # Display the category name instead of its ID
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_name', 
                  'stock_quantity', 'image_url', 'created_date']  # Include specific fields
