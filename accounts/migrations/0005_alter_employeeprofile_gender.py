# Generated by Django 4.0.4 on 2022-04-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employeeprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=100, null=True, verbose_name='Gender'),
        ),
    ]
