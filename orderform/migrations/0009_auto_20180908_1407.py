# Generated by Django 2.0.7 on 2018-09-08 09:07

from django.db import migrations, models
import orderform.models


class Migration(migrations.Migration):

    dependencies = [
        ('orderform', '0008_auto_20180821_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image1',
            field=models.FileField(null=True, upload_to=orderform.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='order',
            name='image2',
            field=models.FileField(null=True, upload_to=orderform.models.user_directory_path),
        ),
    ]
