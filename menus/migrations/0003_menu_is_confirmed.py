# Generated by Django 2.2.4 on 2019-08-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20190823_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='Help easily distinguish status of Menú, False could allow modifications.', verbose_name='confirmed by seller/Nora'),
        ),
    ]
