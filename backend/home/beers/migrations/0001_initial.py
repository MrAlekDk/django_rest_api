# Generated by Django 4.0.6 on 2022-07-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('beer_type', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=44.44, max_digits=15)),
            ],
        ),
    ]