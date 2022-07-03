# Generated by Django 4.0.5 on 2022-07-02 12:28

from django.db import migrations, models
import investors.models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0002_experttraders_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mugshot',
            field=models.ImageField(blank=True, default='', upload_to=investors.models.save_image_investors, verbose_name='Mugshot'),
            preserve_default=False,
        ),
    ]
