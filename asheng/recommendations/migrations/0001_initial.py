# Generated by Django 4.0.3 on 2022-03-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadingUserInputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(null=True)),
                ('genre', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
