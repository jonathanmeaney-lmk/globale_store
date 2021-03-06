# Generated by Django 3.1.7 on 2021-05-06 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='checkout.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
