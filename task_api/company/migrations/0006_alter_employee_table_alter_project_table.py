# Generated by Django 4.1.2 on 2022-10-07 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_department_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]