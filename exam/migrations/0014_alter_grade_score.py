# Generated by Django 3.2.12 on 2022-04-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_exam_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.PositiveSmallIntegerField(default='0', verbose_name='分数'),
        ),
    ]
