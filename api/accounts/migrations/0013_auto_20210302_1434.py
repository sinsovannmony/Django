# Generated by Django 3.1.4 on 2021-03-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210302_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sub_date',
            field=models.DateTimeField(null=True),
        ),
    ]