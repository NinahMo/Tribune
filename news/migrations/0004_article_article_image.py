# Generated by Django 3.1.3 on 2020-11-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201111_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='exit', upload_to='articles/'),
            preserve_default=False,
        ),
    ]
