# Generated by Django 2.2.9 on 2020-02-04 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import problem.models.problem


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagging', '0003_adapt_max_tag_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=64, validators=[problem.models.problem.AliasValidator()], verbose_name='Alias')),
                ('title', models.CharField(blank=True, max_length=192, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('input', models.TextField(blank=True, verbose_name='Input')),
                ('output', models.TextField(blank=True, verbose_name='Output')),
                ('sample', models.TextField(blank=True, verbose_name='Sample')),
                ('hint', models.TextField(blank=True, verbose_name='Hint')),
                ('source', models.CharField(blank=True, max_length=128, verbose_name='Source')),
                ('visible', models.BooleanField(db_index=True, default=False)),
                ('maintaining', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('time_limit', models.IntegerField(default=2000, verbose_name='Time Limit')),
                ('memory_limit', models.IntegerField(default=256, verbose_name='Memory Limit')),
                ('checker', models.CharField(blank=True, max_length=64, verbose_name='Checker')),
                ('interactor', models.CharField(blank=True, max_length=64, verbose_name='Interactor')),
                ('validator', models.CharField(blank=True, max_length=64, verbose_name='Validator')),
                ('pretests', models.TextField(blank=True, verbose_name='Pretest')),
                ('clone_parent', models.PositiveIntegerField(default=0)),
                ('cases', models.TextField(blank=True, verbose_name='Cases')),
                ('points', models.TextField(blank=True, verbose_name='Points')),
                ('group_config', models.TextField(blank=True, default='~', verbose_name='Group')),
                ('template_config', models.TextField(blank=True, default='{}', verbose_name='Template')),
                ('level', models.IntegerField(choices=[(1, 'Naive'), (2, 'Easy'), (3, 'Medium'), (4, 'Hard'), (5, 'Super')], default=3, verbose_name='Difficulty Level')),
                ('ac_user_count', models.PositiveIntegerField(default=0)),
                ('total_user_count', models.PositiveIntegerField(default=0)),
                ('ac_count', models.PositiveIntegerField(default=0)),
                ('total_count', models.PositiveIntegerField(default=0)),
                ('reward', models.FloatField(default=9.9)),
                ('managers', models.ManyToManyField(related_name='managing_problems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('parent_id', models.IntegerField(default=-1)),
                ('problem_list', models.TextField(blank=True)),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialProgram',
            fields=[
                ('fingerprint', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('checker', 'checker'), ('generator', 'generator'), ('interactor', 'interactor'), ('validator', 'validator')], max_length=12)),
                ('filename', models.CharField(max_length=64)),
                ('lang', models.CharField(choices=[('c', 'C'), ('cpp', 'C++11'), ('cc14', 'C++14'), ('cc17', 'C++17'), ('py2', 'Python 2'), ('python', 'Python 3'), ('pypy', 'PyPy'), ('pypy3', 'PyPy 3'), ('java', 'Java 8'), ('pas', 'Pascal'), ('text', 'Text')], default='cc14', max_length=12, verbose_name='language')),
                ('code', models.TextField(blank=True)),
                ('builtin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('parent_id', models.IntegerField(default=-1)),
                ('tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tagging.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackCompare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_1', models.PositiveIntegerField()),
                ('problem_2', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.PositiveIntegerField(db_index=True)),
                ('total_count', models.PositiveIntegerField()),
                ('total_list', models.TextField(blank=True)),
                ('ac_count', models.PositiveIntegerField()),
                ('ac_distinct_count', models.PositiveIntegerField()),
                ('ac_list', models.TextField(blank=True)),
                ('predict_list', models.TextField(blank=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'contest_id')},
            },
        ),
        migrations.CreateModel(
            name='ProblemRewardStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'problem')},
            },
        ),
    ]
