from rest_framework import serializers
from .models import Vendor, PurchaseOrder
from django.utils import timezone
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_on_time_delivery_rate(self, value):
        if not 0.0 <= value <= 100.0:
            raise serializers.ValidationError("On-time delivery rate must be between 0.0 and 100.0.")
        return value

    def validate_quality_rating_avg(self, value):
        if not 0.0 <= value <= 5.0:
            raise serializers.ValidationError("Quality rating average must be between 0.0 and 5.0.")
        return value

    def validate_average_response_time(self, value):
        if value < 0.0:
            raise serializers.ValidationError("Average response time cannot be negative.")
        return value

    def validate_fulfillment_rate(self, value):
        if not 0.0 <= value <= 100.0:
            raise serializers.ValidationError("Fulfillment rate must be between 0.0 and 100.0.")
        return value

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def validate_order_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value

    def validate_delivery_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Delivery date cannot be in the past.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value

    def validate_quality_rating(self, value):
        if value is not None and not 0.0 <= value <= 5.0:
            raise serializers.ValidationError("Quality rating must be between 0.0 and 5.0.")
        return value

    def validate_acknowledgment_date(self, value):
        if value and value < self.instance.issue_date:
            raise serializers.ValidationError("Acknowledgment date cannot be earlier than the issue date.")
        return value

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
