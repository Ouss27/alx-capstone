from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners to edit their profiles.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user
