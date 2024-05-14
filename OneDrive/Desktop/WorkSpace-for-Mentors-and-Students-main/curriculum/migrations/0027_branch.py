# Generated by Django 3.2 on 2021-04-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0026_subject_alloted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
