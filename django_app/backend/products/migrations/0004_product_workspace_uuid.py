# Generated by Django 3.2.16 on 2023-01-13 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '__first__'),
        ('products', '0003_alter_product_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='workspace_uuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workspaces.workspace'),
        ),
    ]
