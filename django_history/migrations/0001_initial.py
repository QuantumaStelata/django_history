# Generated by Django 4.2 on 2023-04-18 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_history.mixins.encoders
import django_history.settings.history


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('created', 'Created'), ('updated', 'Updated'), ('m2m_updated', 'M2M Updated'), ('deleted', 'Deleted')], default='created', max_length=12)),
                ('object_id', models.TextField()),
                ('pre_instance', models.JSONField(encoder=django_history.mixins.encoders.JSONEncoder, null=True)),
                ('post_instance', models.JSONField(encoder=django_history.mixins.encoders.JSONEncoder, null=True)),
                ('instance_changes', models.JSONField(encoder=django_history.mixins.encoders.JSONEncoder, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=django_history.settings.history.current_user_none, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddIndex(
            model_name='history',
            index=models.Index(fields=['content_type', 'object_id'], name='django_hist_content_fd44de_idx'),
        ),
    ]
