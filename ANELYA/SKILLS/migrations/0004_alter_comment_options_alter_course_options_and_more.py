# Generated by Django 5.0.11 on 2025-01-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SKILLS', '0003_alter_comment_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterModelOptions(
            name='courseenrollment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_images/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='lesson_videos/'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table=None,
        ),
        migrations.AlterModelTable(
            name='course',
            table=None,
        ),
        migrations.AlterModelTable(
            name='courseenrollment',
            table=None,
        ),
        migrations.AlterModelTable(
            name='lesson',
            table=None,
        ),
        migrations.AlterModelTable(
            name='module',
            table=None,
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
