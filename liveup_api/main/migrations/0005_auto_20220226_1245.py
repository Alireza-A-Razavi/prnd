# Generated by Django 3.2 on 2022-02-26 09:45

import datetime
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_patient_patient_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 2, 26))]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=datetime.datetime(2022, 2, 26, 9, 45, 59, 941879, tzinfo=utc), error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]