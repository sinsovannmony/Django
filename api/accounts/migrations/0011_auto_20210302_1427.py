# Generated by Django 3.1.4 on 2021-03-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210302_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sub_date',
            field=models.IntegerField(default=0),
        ),
    ]
