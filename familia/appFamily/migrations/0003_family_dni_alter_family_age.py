# Generated by Django 4.0.6 on 2022-07-28 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFamily', '0002_family_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='dni',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
