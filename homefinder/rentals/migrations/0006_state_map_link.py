# Generated by Django 2.0.6 on 2019-06-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_auto_20190622_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='map_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]