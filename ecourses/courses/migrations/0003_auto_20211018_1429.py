# Generated by Django 3.2.8 on 2021-10-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211017_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='courses/%Y/%m')),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Lession',
        ),
        migrations.AddField(
            model_name='lesson',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='courses.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subjects', 'course')},
        ),
    ]
