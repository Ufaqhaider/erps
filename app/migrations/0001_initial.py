# Generated by Django 2.2.3 on 2020-07-29 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAndEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('summary', models.TextField(blank=True, max_length=200, null=True)),
                ('posted_as', models.CharField(choices=[('News', 'News'), ('Event', 'Event')], max_length=10)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=200, unique=True)),
                ('is_current_session', models.BooleanField(blank=True, default=False, null=True)),
                ('next_session_begins', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=10)),
                ('is_current_semester', models.BooleanField(blank=True, default=False, null=True)),
                ('next_semester_begins', models.DateField(blank=True, null=True)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Session')),
            ],
        ),
    ]
