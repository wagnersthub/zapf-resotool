# Generated by Django 2.2.2 on 2019-07-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolution',
            name='reso_type',
            field=models.IntegerField(choices=[(0, 'Resolution'), (1, 'Positionspapier'), (2, 'Selbstverpflichtung')], default=0),
        ),
    ]