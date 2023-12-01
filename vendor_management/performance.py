from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg, F
from .models import PurchaseOrder, Vendor, HistoricalPerformance

def calculate_performance_history(vendor):
    # Calculate On-Time Delivery Rate
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=F('acknowledgment_date')).count()
    total_completed_pos = completed_pos.count()
    on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos > 0 else 0.0

    # Calculate Quality Rating Average
    completed_pos_with_rating = completed_pos.exclude(quality_rating=None)
    quality_rating_average = completed_pos_with_rating.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0.0

    # Calculate Average Response Time
    acknowledged_pos = completed_pos.filter(acknowledgment_date__isnull=False)
    response_times = [po.acknowledgment_date - po.issue_date for po in acknowledged_pos]
    average_response_time = sum(response_times, timedelta()) / len(response_times) if len(response_times) > 0 else timedelta(0)
    average_response_time_hours = average_response_time.total_seconds() / 3600  # convert to hours

    # Calculate Fulfillment Rate
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    successful_fulfillments = total_pos.filter(status='completed').count()
    fulfillment_rate = (successful_fulfillments / total_pos.count()) * 100 if total_pos.count() > 0 else 0.0

    # Create HistoricalPerformance record
    historical_performance = HistoricalPerformance.objects.create(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_average,
        average_response_time=average_response_time_hours,
        fulfillment_rate=fulfillment_rate
    )

    # Update Vendor performance metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_average
    vendor.average_response_time = average_response_time_hours
    vendor.fulfillment_rate = fulfillment_rate

    vendor.save()
    print("Perforamce matrix updated")
    return historical_performance
