from django.shortcuts import render
from . import models


def front_page(request):
    return render(request, 'front_page.html')


def list_table(request):
    tables = models.tables.objects.all()
    return render(request, 'table/list_table.html', {'tables': tables})


def table_def(request, slug):
    columns = models.columns.objects.filter(table_name=slug)
    return render(request, 'table/table_def.html', {'table_name': slug, 'columns': columns})
