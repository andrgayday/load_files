# Generated by Django 3.1.2 on 2020-10-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
    ]
