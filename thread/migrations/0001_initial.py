# Generated by Django 3.2.6 on 2021-08-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=128)),
                ('student_email', models.EmailField(max_length=60)),
                ('address', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
