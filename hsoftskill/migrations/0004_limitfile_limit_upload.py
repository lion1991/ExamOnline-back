# Generated by Django 3.2.12 on 2022-04-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsoftskill', '0003_alter_limitfile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitfile',
            name='limit_upload',
            field=models.IntegerField(default=1, help_text='设定上传开关', verbose_name='设定上传开关'),
            preserve_default=False,
        ),
    ]