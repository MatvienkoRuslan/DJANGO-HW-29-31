# Generated by Django 4.1.5 on 2023-02-11 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='task.category'),
        ),
    ]
