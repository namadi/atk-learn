# Generated by Django 2.1.5 on 2019-02-24 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20190224_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='completed_courses',
            new_name='completed_lessons',
        ),
    ]