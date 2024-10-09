# Generated by Django 5.1.1 on 2024-10-09 15:37

import django.db.models.deletion
import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_diary_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotional',
            name='community_activities',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='community_check',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='drink',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='gratitude_list',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='morning_mood',
            field=models.CharField(blank=True, choices=[('H', 'Happy'), ('O', 'Okay'), ('D', 'Down'), ('S', 'Sad')], default='H', null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='number_of_drinks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='time_spent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='emotional',
            name='vices',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='goals',
            name='goal',
            field=main_app.models.DynamicChoiceField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='image1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='mental',
            name='desires',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mental',
            name='diary_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.diary'),
        ),
        migrations.AlterField(
            model_name='mental',
            name='fears',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mental',
            name='learning_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.goals'),
        ),
        migrations.AlterField(
            model_name='mental',
            name='meditation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='mental',
            name='time_spent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='body_part_worked',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='breakfast',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='dinner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='exercise',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='lunch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='snacks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physical',
            name='workout_link',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
    ]
