# Generated by Django 4.2.17 on 2025-01-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_num', models.IntegerField(unique=True)),
                ('article_item', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('person_accountable', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.CharField(max_length=100)),
                ('date_save', models.DateTimeField(auto_now_add=True)),
                ('make_changes', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
