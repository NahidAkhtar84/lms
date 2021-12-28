# Generated by Django 4.0 on 2021-12-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('voting_date', 'employee')},
        ),
    ]
