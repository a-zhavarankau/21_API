# Generated by Django 4.1.2 on 2022-10-07 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_employee_table_alter_project_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Departmen',
        ),
    ]