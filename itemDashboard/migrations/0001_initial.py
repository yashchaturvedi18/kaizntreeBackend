# Generated by Django 5.0.2 on 2024-02-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
                ('stock_status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=20)),
                ('available_stock', models.IntegerField()),
            ],
        ),
    ]
