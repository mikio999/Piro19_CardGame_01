# Generated by Django 4.2.3 on 2023-07-21 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('mode', models.IntegerField(default=0)),
                ('result', models.IntegerField(default=0)),
                ('my_card', models.IntegerField(default=0)),
                ('player_card', models.IntegerField(default=0)),
                ('my_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.player')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.player', verbose_name='상대')),
            ],
        ),
    ]
