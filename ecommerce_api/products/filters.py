import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # Filter for product name with partial match (case-insensitive)
    name = django_filters.CharFilter(lookup_expr='icontains', label='Product Name')

    # Filter for category with partial match (case-insensitive)
    category = django_filters.CharFilter(field_name='category__name',lookup_expr='icontains', label='Category')

    # Price range filters (min and max prices)
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    class Meta:
        model = Product
        # Allow filtering by name, category, and price range
        fields = ['name', 'category', 'price_min', 'price_max']
