# Generated by Django 5.1.2 on 2024-11-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_commander_ville'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commander',
            name='date_commande',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
