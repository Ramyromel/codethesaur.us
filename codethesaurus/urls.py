"""codethesaurus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
]

handler400 = 'web.views.error_handler_400_bad_request'
handler403 = 'web.views.error_handler_403_forbidden'
handler404 = 'web.views.error_handler_404_not_found'
handler500 = 'web.views.error_handler_500_server_error'
