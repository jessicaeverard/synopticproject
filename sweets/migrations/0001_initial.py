# Generated by Django 4.0.6 on 2022-12-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='sweet/images/')),
            ],
        ),
    ]
