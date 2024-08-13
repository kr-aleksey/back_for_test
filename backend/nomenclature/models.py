from django.db import models


class Nomenclature(models.Model):
    code = models.CharField('Код',
                            max_length=10,
                            unique=True)
    name = models.CharField('Наименование',
                            max_length=100)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'

    def __str__(self):
        return f'{self.code} - {self.name}'
