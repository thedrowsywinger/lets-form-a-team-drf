# Generated by Django 4.1.1 on 2022-09-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_customauthusermodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customauthusermodel",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
