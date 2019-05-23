# Generated by Django 2.1.7 on 2019-03-22 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tongzhidan', '0003_auto_20190322_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='计划发车日期')),
                ('baozhuang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tongzhidan.Baozhuang', verbose_name='包装')),
                ('daozhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tongzhidan.Daozhan', verbose_name='到站')),
                ('fachekehu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tongzhidan.Fachekehu', verbose_name='发车客户')),
                ('guige', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tongzhidan.Guige', verbose_name='规格')),
                ('huowu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tongzhidan.Huowu', verbose_name='货物')),
            ],
            options={
                'verbose_name': '发车计划表',
                'verbose_name_plural': '发车计划表',
            },
        ),
    ]