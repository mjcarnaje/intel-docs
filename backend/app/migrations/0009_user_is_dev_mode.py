# Generated by Django 5.1.2 on 2025-05-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_user_favorite_llm_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dev_mode',
            field=models.BooleanField(default=False, help_text='Whether the user is in dev mode'),
        ),
    ]
