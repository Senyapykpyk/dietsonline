# Generated by Django 4.2 on 2023-05-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profileconsultant_image_profileuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileconsultant',
            old_name='desription',
            new_name='description',
        ),
    ]
