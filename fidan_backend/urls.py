from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import SchoolViewSet, InventoryViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)       
router.register(r'inventory', InventoryViewSet)  
router.register(r'requests', RequestViewSet)    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
]