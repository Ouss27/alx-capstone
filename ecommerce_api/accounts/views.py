from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsOwner
from rest_framework.authentication import TokenAuthentication

# Registration view
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Override permissions to allow access to all users

# retrieve or update view
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Only owners can update their own profile

# delete view
class UserDeleteView(APIView):
    permission_classes = [IsAdminUser]  # Only admin users can delete users

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    """
    Handles user logout by deleting their authentication token.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Delete the user's token
        return Response({"message": "Logged out successfully."}, status=200)