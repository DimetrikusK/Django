# Generated by Django 3.2 on 2021-05-29 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.TextField(db_column='courseNameID')),
                ('isactive', models.IntegerField(db_column='isActive')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('fulldescription', models.TextField(blank=True, db_column='fullDescription', null=True)),
            ],
            options={
                'db_table': 'Course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ecocard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.TextField(db_column='cardNameID')),
                ('isactive', models.IntegerField(db_column='isActive')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('fulldescription', models.TextField(blank=True, db_column='fullDescription', null=True)),
                ('coursenameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco.course')),
            ],
            options={
                'db_table': 'EcoCard',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ecosoviet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cardnameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco.ecocard')),
            ],
            options={
                'db_table': 'EcoSoviet',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eco.profile'),
        ),
    ]
