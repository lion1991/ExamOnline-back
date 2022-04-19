# Generated by Django 2.2.2 on 2022-04-17 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220417_2011'),
        ('question', '0003_auto_20220417_1420'),
        ('exam', '0011_paper_choicemu_number'),
        ('record', '0004_auto_20200425_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choicerecord',
            options={'ordering': ['id'], 'verbose_name': '单选题答题记录', 'verbose_name_plural': '单选题答题记录'},
        ),
        migrations.AlterField(
            model_name='choicerecord',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Choice', verbose_name='单选题'),
        ),
        migrations.CreateModel(
            name='ChoiceMuRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.TextField(blank=True, null=True, verbose_name='你的作答')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Choice', verbose_name='多选题')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='练习')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '多选题答题记录',
                'verbose_name_plural': '多选题答题记录',
                'ordering': ['id'],
            },
        ),
    ]