from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('accounts.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('activities.urls')),
    path('admin/', admin.site.urls)
]
