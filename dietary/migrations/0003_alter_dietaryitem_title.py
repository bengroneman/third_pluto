# Generated by Django 3.2.8 on 2021-10-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietary', '0002_alter_dietaryitem_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietaryitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
