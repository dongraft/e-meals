# Generated by Django 2.2.4 on 2019-08-22 01:57

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Description of the elements that will be part of the dish', verbose_name='Dish description__')),
                ('price', models.PositiveIntegerField(default=0)),
                ('is_enabled', models.BooleanField(default=True, help_text='Help to distinguish the dishes that are enabled from those that are not', verbose_name='is enabled')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date time on which the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
