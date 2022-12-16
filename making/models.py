from django.db import models


class WorkOrder(models.Model):
    number = models.CharField('Номер',
                              max_length=10)
    start_date = models.DateField('Дата начала, план',
                                  blank=True,
                                  null=True)
    is_finished = models.BooleanField('Завершен',
                                      default=False)
    material = models.ForeignKey('nomenclature.Nomenclature',
                                 on_delete=models.PROTECT,
                                 related_name='+',
                                 verbose_name='Сырье')
    product = models.ForeignKey('nomenclature.Nomenclature',
                                on_delete=models.PROTECT,
                                related_name='+',
                                verbose_name='Продукция')

    class Meta:
        verbose_name = 'Наряд на производство'
        verbose_name_plural = 'Наряды на производство'

    def __str__(self):
        return self.number


class Product(models.Model):
    work_order = models.ForeignKey(WorkOrder,
                                   on_delete=models.CASCADE,
                                   related_name='products',
                                   verbose_name='Наряд')
    serial = models.CharField('Серийный номер',
                              max_length=10)
    weight = models.DecimalField('Масса, кг.',
                                 max_digits=6,
                                 decimal_places=3)
    date = models.DateTimeField('Дата производства',
                                auto_now_add=True)

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return f'{self.work_order} - {self.serial}'
