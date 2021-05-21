# Generated by Django 3.2.3 on 2021-05-21 08:17

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0010_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, verbose_name='Название')),
                ('description', tinymce.models.HTMLField(blank=True, default='', verbose_name='Описание курса')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='education.category', verbose_name='Категория')),
                ('responsible', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.mentor', verbose_name='Отвественный')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курс',
            },
        ),
    ]
