# Generated by Django 2.1.3 on 2019-03-28 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certifi', '0003_product_certificate_id_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_certificate',
            name='certific_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='certifi.certificatez'),
        ),
    ]