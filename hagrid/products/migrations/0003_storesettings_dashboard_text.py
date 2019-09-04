# Generated by Django 2.2.4 on 2019-09-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_storesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='storesettings',
            name='dashboard_text',
            field=models.TextField(blank=True, default='', help_text='HTML that will be rendered on the top of the dashboard'),
        ),
    ]