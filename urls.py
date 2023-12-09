from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet
from . import views

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'historical_performance', HistoricalPerformanceViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    # Additional app-specific URLs can be added here
]