# Generated by Django 4.1 on 2022-09-17 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]