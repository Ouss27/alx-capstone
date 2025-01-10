from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


# List and create categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# Retrieve, update, and delete a single category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# List and create products
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# Retrieve, update, and delete a single product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users



#pagination of search and product listing results
class ProductPagination(PageNumberPagination):
    # Set default page size (10 items per page)
    page_size = 10
    # Allow client to set custom page size via query parameter
    page_size_query_param = 'page_size'
    # Set maximum page size limit (e.g., 100)
    max_page_size = 100


#filtering and pagination for the product search and product listing
class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()  # Retrieve all products for filtering/searching
    serializer_class = ProductSerializer  # Use the ProductSerializer for output
    filter_backends = (DjangoFilterBackend, SearchFilter)  # Enable filtering and search
    filterset_class = ProductFilter  # Use the custom filter class
    search_fields = ['name', 'category']  # Enable text search on name and category fields
    pagination_class = ProductPagination  # Apply custom pagination for search results

#product listing with pagination
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()  # Retrieve all products for listing
    serializer_class = ProductSerializer  # Use the ProductSerializer for output
    pagination_class = ProductPagination  # Apply custom pagination for product listing

    # This view does not require filtering; it's just for listing products with pagination