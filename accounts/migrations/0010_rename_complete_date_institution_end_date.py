# Generated by Django 4.0.4 on 2022-05-02 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_employeeprofile_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='complete_date',
            new_name='end_date',
        ),
    ]