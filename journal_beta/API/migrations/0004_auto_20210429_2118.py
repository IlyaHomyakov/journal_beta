# Generated by Django 3.2 on 2021-04-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20210429_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semesteroptions',
            name='semester_end',
        ),
        migrations.RemoveField(
            model_name='semesteroptions',
            name='semester_start',
        ),
        migrations.RemoveField(
            model_name='semesteroptions',
            name='server_week_type_choice',
        ),
        migrations.AddField(
            model_name='group',
            name='group_week_type_choice',
            field=models.CharField(choices=[('1', 'Нечетная'), ('2', 'Четная')], default='1', help_text='Тип недели обязательное значение', max_length=1, verbose_name='Тип текущей учебной недели'),
        ),
    ]
