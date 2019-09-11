# Generated by Django 2.2.5 on 2019-09-06 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('description', models.TextField(verbose_name='О себе')),
                ('linkedin_link', models.CharField(max_length=50, verbose_name='Linkedin')),
                ('github_link', models.CharField(max_length=50, verbose_name='Github')),
                ('website_link', models.CharField(max_length=50, verbose_name='Website')),
                ('email', models.CharField(max_length=75, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_direction', models.CharField(max_length=100, verbose_name='Направление навыка')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Info')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postiton_time', models.CharField(max_length=50, verbose_name='Период работы')),
                ('description', models.TextField(verbose_name='Описание деятельности')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Info')),
            ],
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type_name', models.CharField(max_length=100, verbose_name='Название навыка')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=30, verbose_name='Язык')),
                ('level', models.CharField(max_length=50, verbose_name='Уровень владения')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Info')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=150, verbose_name='Увлечение')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Info')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100, verbose_name='Название учебного заведения')),
                ('degree', models.CharField(max_length=150, verbose_name='Учебная степень')),
                ('study_period', models.CharField(max_length=15, verbose_name='Период обучения')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Info')),
            ],
        ),
    ]
