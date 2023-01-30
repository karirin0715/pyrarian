from django.db import models


class tables(models.Model):
    table_name = models.CharField(max_length=60)
    slug = models.SlugField(null=True)
    rogical_name = models.CharField(max_length=60)
    remark = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class columns(models.Model):
    table_name = models.CharField(max_length=60)
    column_name = models.CharField(max_length=60)
    rogical_name = models.CharField(max_length=60)
    column_type = models.CharField(max_length=20)
