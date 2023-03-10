# Generated by Django 4.1.4 on 2022-12-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0001_initial'),
        ('making', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='nomenclature',
            new_name='product',
        ),
        migrations.AddField(
            model_name='workorder',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='nomenclature.nomenclature', verbose_name='Сырье'),
            preserve_default=False,
        ),
    ]
