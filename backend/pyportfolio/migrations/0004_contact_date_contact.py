# Generated by Django 3.1.1 on 2020-09-22 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pyportfolio', '0003_auto_20200724_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_contact',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
