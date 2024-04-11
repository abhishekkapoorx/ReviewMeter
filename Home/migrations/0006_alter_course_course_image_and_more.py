# Generated by Django 5.0.3 on 2024-04-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_course_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='course_images/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='proof_of_course',
            field=models.FileField(upload_to='course_proof/'),
        ),
    ]
