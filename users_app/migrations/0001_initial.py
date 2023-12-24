# Generated by Django 5.0 on 2023-12-24 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_favorites', models.ManyToManyField(related_name='favorite_by', to='users_app.profiles')),
                ('user_profiles', models.ManyToManyField(related_name='user_profiles', to='users_app.profiles')),
            ],
        ),
        migrations.AddField(
            model_name='profiles',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.users'),
        ),
    ]