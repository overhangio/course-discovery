# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 14:40


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0180_seat_default_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalseat',
            name='currency',
            field=models.ForeignKey(blank=True, db_constraint=False, default='USD', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Currency'),
        ),
    ]
