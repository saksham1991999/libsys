# Generated by Django 2.2.9 on 2020-01-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='previous_year',
            name='exam_category',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previous_year',
            name='exam_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previous_year',
            name='set',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
