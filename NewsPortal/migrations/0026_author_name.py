# Generated by Django 4.1.5 on 2023-04-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0025_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='John Smith', max_length=50),
        ),
    ]
