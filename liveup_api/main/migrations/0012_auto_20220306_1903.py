# Generated by Django 3.2 on 2022-03-06 16:03

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20220227_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admission',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='referral',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='ward',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 3, 6))]),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='end_datetime',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 3, 6, 16, 3, 0, 803707, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='start_datetime',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 3, 6, 16, 3, 0, 803707, tzinfo=utc))]),
        ),
    ]
