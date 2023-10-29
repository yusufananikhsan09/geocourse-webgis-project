"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bikini_bottom.views import home, home_map_api, custom_map_api, facility_form_add, facility_list, facility_form_update, facility_form_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path('api/home-map/', home_map_api, name="home-api"),
    path('api/custom-map/', custom_map_api, name="custom-api"),
    path('facility/add/', facility_form_add, name="facility_form_add"),
    path('facility/', facility_list, name='facility_list'),
    path('facility/update/<int:pk>/', facility_form_update, name='facility_form_update'),
    path('facility/delete/<int:pk>/', facility_form_delete, name='facility_form_delete'),

    # Aunthentication System
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
