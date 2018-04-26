# Generated by Django 2.0.2 on 2018-04-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180402_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_suspend',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='suspend'),
        ),
    ]