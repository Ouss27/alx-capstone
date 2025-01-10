from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView, 
    ProductSearchView, ProductListView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/login/', obtain_auth_token, name='api_token_auth'),  # For token login
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),#category list or create
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),#category Retrieve,Update or Delete
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),#product list or create
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),#product Retrieve,Update or Delete
    path('products/search/', ProductSearchView.as_view(), name='product-search'),#product search with filters (name, category, price range)
    path('products/list/', ProductListView.as_view(), name='product-list'),#product listing (with pagination)
]

