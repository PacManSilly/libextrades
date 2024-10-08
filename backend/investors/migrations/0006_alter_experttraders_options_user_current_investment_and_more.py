# Generated by Django 4.0.5 on 2022-07-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0005_alter_user_mugshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experttraders',
            options={'verbose_name_plural': 'ExpertTraders'},
        ),
        migrations.AddField(
            model_name='user',
            name='current_investment',
            field=models.CharField(blank=True, default='0.00', help_text='Investors currrent investment', max_length=50, verbose_name='Current Investment'),
        ),
        migrations.AddField(
            model_name='user',
            name='total_balance',
            field=models.CharField(blank=True, default='0.00', help_text='Investors total balance', max_length=50, verbose_name='Total Balance'),
        ),
        migrations.AddField(
            model_name='user',
            name='total_earnings',
            field=models.CharField(blank=True, default='0.00', help_text='Investors total earnings', max_length=50, verbose_name='Total Earnings'),
        ),
        migrations.AddField(
            model_name='user',
            name='total_investment',
            field=models.CharField(blank=True, default='0.00', help_text='Investors total investment', max_length=50, verbose_name='Total Investment'),
        ),
    ]
