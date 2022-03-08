# Generated by Django 4.0.2 on 2022-03-05 00:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('gender', models.CharField(blank=True, max_length=20, null=True, verbose_name='Gender')),
                ('workspace', models.CharField(blank=True, max_length=100, null=True, verbose_name='Work Space')),
                ('city_population', models.CharField(blank=True, max_length=50, null=True, verbose_name='City Population')),
                ('average_weekly_sleep_hrs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Average Weekly Sleep Hours')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Challenge',
                'verbose_name_plural': 'Challenges',
                'db_table': 'challenges',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('description', models.TextField(verbose_name='Description')),
                ('origin', models.CharField(choices=[('Personal Experience', 'Personal Experience'), ('Book', 'Book'), ('Lecture', 'Lecture'), ('Film', 'Film'), ('Theater Play', 'Theater Play'), ('Video', 'Video'), ('Video Game', 'Video Game'), ('Song', 'Song'), ('Article', 'Article'), ('Relation', 'Relation'), ('Lesson', 'Lesson'), ('Interpretation', 'Interpretation'), ('Other', 'Other')], max_length=100, verbose_name='Origin')),
                ('domain', models.CharField(blank=True, choices=[('Computer Science', 'Computer Science'), ('Physics', 'Physics'), ('Philosophy', 'Philosophy'), ('Design', 'Design'), ('Art', 'Art'), ('Electrical Engineering', 'Electrical Engineering'), ('Software Engineering', 'Software Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Mechanical Engineering', 'Mehcanical Engineering'), ('Biology', 'Biology'), ('Chemestry', 'Chemestry'), ('Mathematics', 'Mathematics'), ('Literature', 'Literature'), ('Music', 'Music'), ('Law', 'Law'), ('Business', 'Business'), ('Economics', 'Economics'), ('Political Science', 'Political Science'), ('Arquitecture', 'Arquitecture'), ('Anthropology', 'Anthropology'), ('Medicine', 'Medicine'), ('Education', 'Education'), ('Other', 'Other')], max_length=100, null=True, verbose_name='Domain')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('explanation', models.TextField(verbose_name='Explanation')),
                ('type', models.CharField(blank=True, choices=[('Could Benefit From', 'Could Benefit From'), ('Could Solve', 'Could Solve'), ('Could Combine To Create', 'Could Combine To Create'), ('Could Contrast To Create', 'Could Contrast To Create'), ('Could Be A Cause', 'Could Cause Be A Cause')], max_length=50, null=True, verbose_name='Type')),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generalizing_core.challenge', verbose_name='Challenge')),
                ('lessons', models.ManyToManyField(to='generalizing_core.Lesson', verbose_name='Lessons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Relation',
                'verbose_name_plural': 'Relations',
                'db_table': 'relations',
            },
        ),
        migrations.CreateModel(
            name='RelationContext',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('place', models.CharField(blank=True, max_length=240, null=True, verbose_name='Place')),
                ('dialogued', models.BooleanField(blank=True, null=True, verbose_name='Dialogued')),
                ('daydreamed', models.BooleanField(blank=True, null=True, verbose_name='Day Dreamed')),
                ('past_week_sleep_hrs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Past Week Sleep Hours')),
                ('mood', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mood')),
                ('relaxation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Relaxation')),
                ('iterations', models.IntegerField(blank=True, null=True, verbose_name='Iterations')),
            ],
            options={
                'verbose_name': 'Relation Context',
                'verbose_name_plural': 'Relations Contexts',
                'db_table': 'relations_contexts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='RelationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('relation', models.ForeignKey(db_column='relation', on_delete=django.db.models.deletion.CASCADE, to='generalizing_core.relation', verbose_name='Relation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonFile',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('lesson', models.ForeignKey(db_column='lesson', on_delete=django.db.models.deletion.CASCADE, to='generalizing_core.lesson', verbose_name='Lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, to='generalizing_core.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True)),
                ('area', models.CharField(blank=True, choices=[('Computer Science', 'Computer Science'), ('Physics', 'Physics'), ('Philosophy', 'Philosophy'), ('Design', 'Design'), ('Art', 'Art'), ('Electrical Engineering', 'Electrical Engineering'), ('Software Engineering', 'Software Engineering'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Mechanical Engineering', 'Mehcanical Engineering'), ('Biology', 'Biology'), ('Chemestry', 'Chemestry'), ('Mathematics', 'Mathematics'), ('Literature', 'Literature'), ('Music', 'Music'), ('Law', 'Law'), ('Business', 'Business'), ('Economics', 'Economics'), ('Political Science', 'Political Science'), ('Arquitecture', 'Arquitecture'), ('Anthropology', 'Anthropology'), ('Medicine', 'Medicine'), ('Education', 'Education'), ('Other', 'Other')], max_length=100, null=True, verbose_name='Domain')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Expertise',
                'verbose_name_plural': 'Expertises',
                'db_table': 'expertises',
            },
        ),
        migrations.AddField(
            model_name='challenge',
            name='lesson_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson_1', to='generalizing_core.lesson', verbose_name='Lesson 1'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='lesson_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson_2', to='generalizing_core.lesson', verbose_name='Lesson 2'),
        ),
    ]