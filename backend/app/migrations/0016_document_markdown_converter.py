# Generated by Django 5.1.2 on 2024-12-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='markdown_converter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
