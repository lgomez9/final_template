# Generated by Django 3.1.3 on 2022-02-16 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220216_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_grade',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='lesson_id',
        ),
    ]
