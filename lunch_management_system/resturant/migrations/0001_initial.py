# Generated by Django 4.0 on 2021-12-29 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(class)s_related', to='auth.user')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_by_%(class)s_related', to='auth.user')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(class)s_related', to='auth.user')),
            ],
            options={
                'db_table': 'resturants',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ResturantMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250)),
                ('menu_date', models.DateField()),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(class)s_related', to='auth.user')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_by_%(class)s_related', to='auth.user')),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='resturant_menus', to='resturant.resturant')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(class)s_related', to='auth.user')),
            ],
            options={
                'db_table': 'resturant_menus',
                'ordering': ['id'],
                'unique_together': {('menu_date', 'resturant')},
            },
        ),
        migrations.CreateModel(
            name='ResturantMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('resturant_menu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='resturant_menu_item', to='resturant.resturantmenu')),
            ],
            options={
                'db_table': 'resturant_menu_items',
                'ordering': ['id'],
                'unique_together': {('name', 'resturant_menu_id')},
            },
        ),
        migrations.CreateModel(
            name='ChampionResturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_%(class)s_related', to='auth.user')),
                ('deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_by_%(class)s_related', to='auth.user')),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='champio_resturant', to='resturant.resturant')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_%(class)s_related', to='auth.user')),
            ],
            options={
                'db_table': 'champion_resturants',
                'ordering': ['id'],
                'unique_together': {('date', 'resturant')},
            },
        ),
    ]
