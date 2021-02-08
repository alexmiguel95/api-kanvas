from rest_framework.permissions import BasePermission


class InstructorOrFacilitadorOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" or request.method == "GET":
            return True

        if request.method == "PUT":
            return request.user.is_staff
