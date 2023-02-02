# Generated by Django 3.2.16 on 2023-01-13 02:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('workspace_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, null=True)),
                ('polygon', models.JSONField(null=True)),
                ('coordinates', models.JSONField(null=True)),
                ('type', models.CharField(choices=[('Closet', 'CLOSET'), ('Cabinet', 'CABINET'), ('Shelf', 'sHELF')], max_length=30, null=True)),
                ('ioCrossline', models.JSONField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'workspaces',
            },
        ),
    ]
