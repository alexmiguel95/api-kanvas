from django.urls import path
from .views import CourseView, CourseUpdateView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/registrations/", CourseUpdateView.as_view()),
]
