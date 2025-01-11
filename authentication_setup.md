# E-commerce Product API

## Authentication Setup

### Overview
The API uses two authentication mechanisms:
1. **SessionAuthentication:** Ideal for web-based clients and enables using the Django session framework for authentication.
2. **TokenAuthentication:** Suitable for external or mobile clients. Each user is issued a token for API access.

---

### Configuration

#### 1. Authentication Classes
In the `settings.py` file:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # For web sessions
        'rest_framework.authentication.TokenAuthentication',    # For API tokens
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # Default permission
    ],
}
```

#### 2. Token Authentication
To generate tokens for users:
- Ensure the `authtoken` app is installed:
  ```python
  INSTALLED_APPS = [
      ...
      'rest_framework.authtoken',
  ]
  ```
- Use the token endpoint:
  ```http
  POST /api/accounts/login/
  Content-Type: application/json

  {
      "username": "testuser",
      "password": "testpassword"
  }
  ```

  Response:
  ```json
  {
      "token": "abc123xyz456"
  }
  ```

#### 3. Securing Endpoints
Use `IsAuthenticatedOrReadOnly` permission to secure views. Example:
```python
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Retrieve, update, and delete a single product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users
```

---

### Testing Authentication

#### SessionAuthentication
- Log in to the browsable API using `/auth/login/`.
- Access secure endpoints through the session.

#### TokenAuthentication
- Use the obtained token in the `Authorization` header for API requests:
  ```http
  Authorization: Token abc123xyz456
  ```

---

### Example Secure Endpoints

- **Protected Product Management:**
  Only authenticated users can create, update, or delete products.
  ```http
  POST /api/products/
  Authorization: Token abc123xyz456

  {
      "name": "Product A",
      "price": 20.0,
      "category": "Books",
      "stock_quantity": 50
  }
  ```

  Response:
  ```json
  {
      "id": 1,
      "name": "Product A",
      "price": 20.0,
      "category": "Books",
      "stock_quantity": 50
  }
  ```

---


