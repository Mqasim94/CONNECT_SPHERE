# Generated by Django 5.0 on 2024-01-18 18:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField()),
                ('replied_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('replier_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.comment')),
            ],
        ),
    ]
