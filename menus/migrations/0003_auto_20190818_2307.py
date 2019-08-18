# Generated by Django 2.2.4 on 2019-08-18 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20190816_0255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'get_latest_by': 'created_at', 'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date time on which the object was created.'),
        ),
        migrations.AddField(
            model_name='menu',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]