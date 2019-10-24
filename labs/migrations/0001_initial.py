# Generated by Django 2.2.1 on 2019-10-24 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование категории профессии')),
            ],
            options={
                'verbose_name': 'Категория профессий',
                'verbose_name_plural': 'Категории профессий',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование профессии')),
                ('count', models.IntegerField(verbose_name='Количество работников данной професии')),
                ('first_shift_count', models.IntegerField(verbose_name='Количество работников в первую смену')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.ProfessionCategory')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]