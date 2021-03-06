# Generated by Django 4.0 on 2021-12-29 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('resturant', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='resturant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='voted_resturant', to='resturant.resturant'),
        ),
        migrations.AddField(
            model_name='vote',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(class)s_related', to='auth.user'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('voting_date', 'employee')},
        ),
    ]
