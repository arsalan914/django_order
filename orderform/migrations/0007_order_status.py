# Generated by Django 2.0.7 on 2018-08-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderform', '0006_auto_20180805_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not-Accepted'), (1, 'Accepted'), (2, 'Ready-for-delivery'), (3, 'Completed')], default=0),
        ),
    ]
