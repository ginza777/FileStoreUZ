# Generated by Django 3.2.6 on 2022-04-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_books_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(blank=True, default='yrJopkWnBXYFaKzvDwTS', max_length=300, null=True),
        ),
    ]