# Generated by Django 3.2.8 on 2021-10-20 07:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='upload/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='upload/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatar/%Y/%m'),
        ),
    ]