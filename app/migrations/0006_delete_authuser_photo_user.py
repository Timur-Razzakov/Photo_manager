# Generated by Django 4.1.4 on 2022-12-15 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_photo_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
