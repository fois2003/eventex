# Generated by Django 2.0.6 on 2018-09-08 12:05

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False


    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]
