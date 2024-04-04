# Generated by Django 5.0.3 on 2024-03-29 10:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugreport',
            name='priority',
            field=models.IntegerField(default=1, verbose_name=(1, 2, 3, 4, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bugreport',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bugreport',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='priority',
            field=models.IntegerField(default=1, verbose_name=(1, 2, 3, 4, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='status',
            field=models.CharField(choices=[('Consideration', 'Рассмотрение'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')], default='Рассмотрение', max_length=100),
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.task'),
        ),
    ]
