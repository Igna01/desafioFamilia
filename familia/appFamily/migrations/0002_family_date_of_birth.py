# Generated by Django 4.0.6 on 2022-07-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFamily', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
