# Generated by Django 3.2.3 on 2021-06-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_skillmodel_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年齢'),
        ),
    ]
