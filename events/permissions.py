from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    """Custom permission to allow only users with 'admin' role to create events."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class IsUserRole(permissions.BasePermission):
    """Custom permission to allow only users with 'user' role to purchase tickets."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "user"
