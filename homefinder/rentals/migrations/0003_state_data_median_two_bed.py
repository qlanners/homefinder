# Generated by Django 2.0.6 on 2019-06-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_state_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='state_data',
            name='median_two_bed',
            field=models.IntegerField(null=True),
        ),
    ]
