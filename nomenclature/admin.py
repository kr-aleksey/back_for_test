from django.contrib import admin

from nomenclature.models import Nomenclature


@admin.register(Nomenclature)
class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = ('code', )
    search_fields = ('code', 'name',)
    fields = ('id', 'code', 'name',)
    readonly_fields = ('id', )
