# Generated by Django 3.2.3 on 2021-05-29 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20210529_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={},
        ),
        migrations.RenameField(
            model_name='blogmodel',
            old_name='updated_at',
            new_name='upload_to',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
