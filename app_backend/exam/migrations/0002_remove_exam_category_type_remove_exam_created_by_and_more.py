# Generated by Django 4.1.5 on 2023-11-04 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exam",
            name="category_type",
        ),
        migrations.RemoveField(
            model_name="exam",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="question",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="question",
            name="difficulty_level",
        ),
        migrations.RemoveField(
            model_name="question",
            name="question_tag",
        ),
        migrations.RemoveField(
            model_name="question",
            name="question_type",
        ),
        migrations.RemoveField(
            model_name="user",
            name="role_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="status_name",
        ),
    ]
