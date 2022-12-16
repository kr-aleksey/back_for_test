from random import randint

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework import filters

from making.models import WorkOrder, Product
from nomenclature.models import Nomenclature
from .serializers import (WorkOrderReadSerializer,
                          WorkOrderWriteSerializer,
                          NomenclatureSerializer,
                          ProductSerializer)


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.select_related('material', 'product')
    serializer_class = WorkOrderReadSerializer
    ordering = ('start_date',)

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter,)
    ordering_fields = ('number', 'start_date', 'is_finished',)
    filterset_fields = ('start_date', 'is_finished', 'product__id',)
    search_fields = ('number',
                     'material__name',
                     'material__code',
                     'product__name',
                     'product__code',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkOrderReadSerializer
        return WorkOrderWriteSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None

    def get_work_order(self):
        return get_object_or_404(WorkOrder,
                                 pk=self.kwargs['work_order_id'])

    def get_queryset(self):
        work_order = self.get_work_order()
        return work_order.products.order_by('date')

    def perform_create(self, serializer):
        work_order = self.get_work_order()
        if work_order.is_finished:
            raise PermissionDenied
        serializer.save(work_order=work_order,
                        serial=f'{randint(10000, 99999)}-RND')


class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer
    ordering = ('code',)

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter,)
    ordering_fields = ('code', 'name',)
    filterset_fields = ('code',)
    search_fields = ('code', 'name',)
