# Generated by Django 2.2.2 on 2020-06-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]