# Generated by Django 5.2.4 on 2025-07-07 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated'), ('Checked', 'Checked'), ('Unchecked', 'Unchecked'), ('Deleted', 'Deleted')], max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('details', models.TextField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notesapp.todo')),
            ],
        ),
    ]
