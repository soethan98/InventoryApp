# Generated by Django 5.1.4 on 2024-12-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('quality', models.IntegerField()),
                ('supplier', models.CharField(max_length=100)),
            ],
        ),
    ]
