# Generated by Django 2.2.3 on 2019-07-23 11:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20190723_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
