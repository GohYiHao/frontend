# Generated by Django 4.2.10 on 2024-03-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replicate', '0005_alter_replicatedata_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replicatedata',
            name='key',
            field=models.IntegerField(default=1),
        ),
    ]
