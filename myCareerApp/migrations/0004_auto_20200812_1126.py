# Generated by Django 3.0.8 on 2020-08-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCareerApp', '0003_auto_20200812_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='생년월일'),
        ),
    ]