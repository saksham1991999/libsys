# Generated by Django 2.2.9 on 2020-01-29 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200129_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug_report',
            options={'verbose_name_plural': 'Bug Reports'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'FAQ'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name_plural': 'Newsletter Subscribers'},
        ),
        migrations.AlterModelOptions(
            name='termsandconditions',
            options={'verbose_name_plural': 'Terms And Conditions'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterModelOptions(
            name='weekday',
            options={'verbose_name_plural': 'Weekdays'},
        ),
        migrations.CreateModel(
            name='comaprison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libraries', models.ManyToManyField(to='core.library')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comparison of Libraries',
            },
        ),
    ]