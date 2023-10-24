from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam.urls')),
    path('', include('users.urls')),
    path('', include('results.urls')),
]

# Include Django's authentication URLs
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
