# Generated by Django 3.0.8 on 2020-07-12 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL)),
                ('follower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
