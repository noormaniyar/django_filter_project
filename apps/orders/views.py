from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter
from django.shortcuts import render
from django.views.generic import TemplateView


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get(self, request, *args, **kwargs):
        filterset = self.filterset_class(request.GET, queryset=self.get_queryset())
        
        context = {
            'orders': filterset.qs,
            'request': request,
        }
        return render(request, 'orders/orders_list.html', context=context)
