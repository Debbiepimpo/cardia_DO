from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'order'})),
    path('<int:pk>/', OrderViewSet.as_view({'get': 'retrieve'})),
    path('add-order/', OrderViewSet.as_view({'post': 'create'})),
    path('update-order/<int:pk>/', OrderViewSet.as_view({'patch': 'update'})),
    path('delete-order/<int:pk>/', OrderViewSet.as_view({'delete': 'destroy'})),
    path('', include(router.urls)),
]