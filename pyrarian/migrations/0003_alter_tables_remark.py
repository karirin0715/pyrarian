# Generated by Django 4.1.5 on 2023-01-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyrarian', '0002_remove_tables_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
