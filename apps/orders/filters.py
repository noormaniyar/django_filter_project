import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name='total_amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='total_amount', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date_created', lookup_expr='lte')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['min_amount', 'max_amount', 'start_date', 'end_date', 'status']
