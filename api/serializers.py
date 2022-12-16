from rest_framework import serializers

from making.models import WorkOrder, Product
from nomenclature.models import Nomenclature


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = (
            'id',
            'code',
            'name',
        )
        read_only_fields = ('id',)


class WorkOrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = (
            'id',
            'number',
            'start_date',
            'material',
            'product',
            'is_finished',
        )
        read_only_fields = ('id',)


class WorkOrderReadSerializer(WorkOrderWriteSerializer):
    material = NomenclatureSerializer(read_only=True)
    product = NomenclatureSerializer(read_only=True)

    class Meta(WorkOrderWriteSerializer.Meta):
        pass


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'serial',
            'weight',
            'date',
        )
        read_only_fields = ('id', 'serial', 'date')
