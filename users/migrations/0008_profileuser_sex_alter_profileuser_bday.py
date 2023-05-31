# Generated by Django 4.2 on 2023-05-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_desription_profileconsultant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='sex',
            field=models.TextField(max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='bday',
            field=models.DateField(default='1990-01-01', verbose_name='Дата рождения'),
        ),
    ]
