# Generated by Django 3.0.6 on 2020-05-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiLoginUserData',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.TextField(blank=True, null=True)),
                ('mark_attandance', models.BooleanField(default=True)),
            ],
        ),
    ]