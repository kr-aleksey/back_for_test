from django.contrib import admin

from making.models import WorkOrder, Product


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_finished', 'start_date', 'product', )
    list_filter = ('is_finished', )
    search_fields = ('number', 'product__code', 'product__name')
    fields = ('id',
              'number',
              'start_date',
              'is_finished',
              'material',
              'product')
    readonly_fields = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('serial', 'work_order', 'weight')
    search_fields = ('serial', 'work_order__number')
    fields = ('id', 'work_order', 'serial', 'weight', 'date')
    readonly_fields = ('id', 'work_order', 'date')
