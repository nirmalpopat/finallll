# Generated by Django 3.2.4 on 2021-07-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0012_auto_20210708_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='pri',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
