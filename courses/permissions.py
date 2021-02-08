from rest_framework.permissions import BasePermission


class InstructorOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        if request.method == "POST" or request.method == "PUT":
            return request.user.is_superuser
