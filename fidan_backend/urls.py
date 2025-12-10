from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import SchoolViewSet, InventoryViewSet, RequestViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)       
router.register(r'inventory', InventoryViewSet)  
router.register(r'requests', RequestViewSet)  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('yusuf/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]