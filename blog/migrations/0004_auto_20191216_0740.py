# Generated by Django 3.0 on 2019-12-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191216_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
