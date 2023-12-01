# vendor_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/', views.PurchaseOrderListView.as_view(), name='purchaseorder-list'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchaseorder-detail'),
    path('purchase_orders/<int:pk>/acknowledge/', views.AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchaseorder'),
    ]
