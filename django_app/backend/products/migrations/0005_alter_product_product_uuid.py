# Generated by Django 3.2.16 on 2023-01-13 03:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_workspace_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_uuid',
            field=models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False),
        ),
    ]
