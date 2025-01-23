from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('add-product/', ProductViewSet.as_view({'post': 'create'})),
    path('update-product/<int:pk>/', ProductViewSet.as_view({'patch': 'update'})),
    path('delete-product/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'})),
    path('', include(router.urls)),
]