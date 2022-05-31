# Generated by Django 3.2.12 on 2022-05-04 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.classroom'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.course'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.teacher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.teacher'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='classroom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.classroom'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='courses',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.TextField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.TextField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
