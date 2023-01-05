# Generated by Django 4.0.6 on 2022-12-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weightPerSweet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.FloatField()),
                ('quantityInGrams', models.IntegerField()),
            ],
        ),
    ]