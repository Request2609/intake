# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 19:08
from __future__ import unicode_literals

from django.db import migrations, models
from intake.models.form_submission import FORMSUBMISSION_TEXT_SEARCH_FIELDS


def copy_answers_to_fields(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    FormSubmission = apps.get_model('intake', 'FormSubmission')
    subs = FormSubmission.objects.using(db_alias).all()
    keys = FORMSUBMISSION_TEXT_SEARCH_FIELDS
    for sub in subs:
        for key in keys:
            existing = sub.answers.get(key, "")
            setattr(sub, key, existing)
        sub.save()


def empty_new_answers_fields(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    FormSubmission = apps.get_model('intake', 'FormSubmission')
    subs = FormSubmission.objects.using(db_alias).all()
    keys = FORMSUBMISSION_TEXT_SEARCH_FIELDS
    for sub in subs:
        for key in keys:
            setattr(sub, key, "")
        sub.save()


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0046_add_other_next_steps_to_status_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='alternate_phone_number',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='case_number',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='drivers_license_or_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='email',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='first_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='last_four',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='last_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='phone_number',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='ssn',
            field=models.TextField(default=''),
        ),
        migrations.RunPython(copy_answers_to_fields, empty_new_answers_fields),
    ]