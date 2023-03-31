# Generated by Django 3.2.12 on 2023-03-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsoftskill', '0004_linuxscore3_linuxscore4_linuxscore5_linuxscore6_linuxscore7_linuxscore8_linuxscore9_networkscore3_ne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('linux_score', models.FloatField(blank=True, null=True, verbose_name='服务器成绩')),
                ('period', models.IntegerField(default=9, verbose_name='考核期数')),
            ],
            options={
                'verbose_name': '总成绩10',
                'verbose_name_plural': '总成绩10',
                'db_table': 'exam_score_total_10',
                'unique_together': {('name', 'period')},
            },
        ),
        migrations.CreateModel(
            name='LinuxScore10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('period', models.IntegerField(default=10, verbose_name='考核期数')),
                ('item1', models.FloatField(blank=True, null=True, verbose_name='开机启动vsftpd服务(5分)')),
                ('item2', models.FloatField(blank=True, null=True, verbose_name='设置ftp登陆公告(5分)')),
                ('item3', models.FloatField(blank=True, null=True, verbose_name='匿名用户权限(20分)')),
                ('item4', models.FloatField(blank=True, null=True, verbose_name='本地用户权限(10分)')),
                ('item5', models.FloatField(blank=True, null=True, verbose_name='ftpuser1用户权限(20分)')),
                ('item6', models.FloatField(blank=True, null=True, verbose_name='ftpuser2用户权限(20分)')),
                ('item7', models.FloatField(blank=True, null=True, verbose_name='用户限速配置(10分)')),
                ('item8', models.FloatField(blank=True, null=True, verbose_name='用户连接数限制配置(10分)')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='总分')),
            ],
            options={
                'verbose_name': '服务器成绩10',
                'verbose_name_plural': '服务器成绩10',
                'db_table': 'exam_score_linux_10',
                'unique_together': {('name', 'period')},
            },
        ),
    ]