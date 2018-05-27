# Generated by Django 2.0.5 on 2018-05-27 06:21

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('record_date', models.DateField(default=datetime.date.today, help_text='Date of the DayEntry', unique=True)),
                ('day_summary', models.TextField(blank=True, help_text='Summary for the day', null=True)),
                ('scrum_summary', models.TextField(blank=True, help_text='Summary for the *Work* day', null=True)),
                ('time_logged', models.PositiveSmallIntegerField(blank=True, help_text='Total time logged in the day in minutes', null=True, validators=[django.core.validators.MaxValueValidator(1440, message="You can't log more than 24 hours in a day")])),
            ],
            options={
                'verbose_name_plural': 'Day Entries',
            },
        ),
        migrations.CreateModel(
            name='DayEntryTagStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_logged', models.PositiveSmallIntegerField(help_text='Total time logged in the day, for the tag, in minutes', validators=[django.core.validators.MaxValueValidator(1440, message="You can't log more than 24 hours in a day")])),
                ('day_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DayEntry')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('response', models.TextField(blank=True, null=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('day_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DayEntry')),
            ],
            options={
                'verbose_name_plural': 'Journal Entries',
            },
        ),
        migrations.CreateModel(
            name='JournalEntryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('title', models.CharField(help_text='What do you want to answer?', max_length=128)),
                ('response', models.TextField(blank=True, help_text='Template for the response. Whatever is specified here will be copied to the day entry as is.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ManualTimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('duration', models.PositiveSmallIntegerField(help_text='Time in minutes', validators=[django.core.validators.MaxValueValidator(1440, message="You can't log more than 24 hours in a day")])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepeatingScrumEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Repeating Scrum Entries',
            },
        ),
        migrations.CreateModel(
            name='ScrumEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('title', models.CharField(help_text='What task do you have to do?', max_length=128)),
                ('notes', models.TextField()),
                ('final_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Completed'), (2, 'Incomplete'), (3, 'Dropped')], null=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('day_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DayEntry')),
                ('repeated_scrum_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.RepeatingScrumEntry')),
            ],
            options={
                'verbose_name_plural': 'Scrum Entries',
            },
        ),
        migrations.CreateModel(
            name='StartEndTimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('scrum_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ScrumEntry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('name', models.SlugField(max_length=32, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='scrumentry',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='repeatingscrumentry',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='manualtimelog',
            name='scrum_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ScrumEntry'),
        ),
        migrations.AddField(
            model_name='journalentrytemplate',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.JournalEntryTemplate'),
        ),
        migrations.AddField(
            model_name='dayentrytagstat',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tag'),
        ),
        migrations.AddField(
            model_name='dayentry',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]