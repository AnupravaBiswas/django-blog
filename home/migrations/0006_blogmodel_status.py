# Generated by Django 3.2.3 on 2021-05-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blogmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
