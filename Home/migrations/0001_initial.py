# Generated by Django 5.0.3 on 2024-04-07 06:21

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(default='', max_length=500)),
                ('course_description', models.TextField(default='', max_length=5000)),
                ('no_of_modules', models.IntegerField(default=0)),
                ('module_content', models.TextField(default='', max_length=5000)),
                ('author', models.CharField(default='', max_length=50)),
                ('published_date', models.DateField(default=datetime.datetime.now)),
                ('course_image', models.ImageField(default='course_images/default.png', upload_to='course_images')),
                ('course_url', models.URLField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('overall_rating', models.IntegerField(default=0)),
                ('relevence', models.IntegerField(default=0)),
                ('content_quality', models.IntegerField(default=0)),
                ('instructor_expertise', models.IntegerField(default=0)),
                ('engagement', models.IntegerField(default=0)),
                ('clarity_of_explanation', models.IntegerField(default=0)),
                ('practical_application', models.IntegerField(default=0)),
                ('support_resources', models.IntegerField(default=0)),
                ('feedback_and_assessment', models.IntegerField(default=0)),
                ('flexibility', models.IntegerField(default=0)),
                ('community_and_networking_opportunities', models.IntegerField(default=0)),
                ('value_for_money', models.IntegerField(default=0)),
                ('accepted', models.BooleanField(default=False)),
                ('proof_of_course', models.FileField(default='course_proof/default1712470887.686912.png', upload_to='course_images')),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Home.course')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
