# Generated by Django 3.2.8 on 2021-10-19 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('cost', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('shelf_life', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('department', models.CharField(max_length=40)),
                ('facility', models.CharField(max_length=40)),
                ('dietary_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dietary.dietaryitem')),
            ],
        ),
    ]
