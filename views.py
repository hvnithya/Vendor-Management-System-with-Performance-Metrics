from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .seralization import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.views.generic import TemplateView


# Create your views here.
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HomeView(TemplateView):
    template_name = 'index.html'