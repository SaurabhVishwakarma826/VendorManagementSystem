from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.utils import timezone
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views import View
from django.shortcuts import get_object_or_404
class VendorListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

class PurchaseOrderListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    def retrieve(self, request, *args, **kwargs):
        po_number = kwargs.get('pk')
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(purchase_order)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        po_id = kwargs.get('pk')
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(purchase_order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        po_id = kwargs.get('pk')
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AcknowledgePurchaseOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        purchase_order = get_object_or_404(PurchaseOrder, po_number=pk)

        # Check if the current user is the vendor associated with the purchase order
        # if request.user != purchase_order.vendor.user:
        #     return Response({'detail': 'You do not have permission to acknowledge this purchase order.'},
        #                     status=status.HTTP_403_FORBIDDEN)

        # Update acknowledgment_date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Optionally, you can recalculate vendor performance metrics here

        serializer = PurchaseOrderSerializer(purchase_order)
        data = {"po_number":pk,"ackTime": timezone.now()}
        return Response(data)


