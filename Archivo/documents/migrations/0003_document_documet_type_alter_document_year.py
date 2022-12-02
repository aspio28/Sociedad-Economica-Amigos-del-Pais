# Generated by Django 4.1.2 on 2022-12-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='documet_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
