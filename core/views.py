from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from core.models import Order

from core.serializers import OrderSerializer


# Create your views here.


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser, ]
    queryset = Order.objects.all()
