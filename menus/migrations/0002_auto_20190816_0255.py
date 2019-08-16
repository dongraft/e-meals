# Generated by Django 2.2.4 on 2019-08-16 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudishes',
            name='dishe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.Dishe'),
        ),
        migrations.AlterField(
            model_name='menudishes',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu'),
        ),
        migrations.AlterUniqueTogether(
            name='menudishes',
            unique_together={('menu', 'dishe')},
        ),
    ]
