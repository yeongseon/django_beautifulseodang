# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('title', models.CharField(max_length=1024)),
                ('body', models.CharField(max_length=4096)),
                ('auth', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
