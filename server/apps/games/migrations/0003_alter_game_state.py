# Generated by Django 4.2.3 on 2023-07-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
