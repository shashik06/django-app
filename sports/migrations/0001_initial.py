# Generated by Django 4.2.6 on 2023-12-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('tags', models.CharField(max_length=50)),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='sports/')),
            ],
        ),
    ]
