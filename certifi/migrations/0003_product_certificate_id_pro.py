# Generated by Django 2.1.3 on 2019-03-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifi', '0002_certificatez_sequence_cer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_certificate',
            name='id_pro',
            field=models.IntegerField(default=1),
        ),
    ]
