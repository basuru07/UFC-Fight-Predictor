# Generated by Django 5.2 on 2025-04-05 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('win_streak', models.IntegerField(default=0)),
                ('lose_streak', models.IntegerField(default=0)),
                ('avg_sig_strikes_landed', models.FloatField(default=0)),
                ('avg_sig_strikes_pct', models.FloatField(default=0)),
                ('avg_takedowns_landed', models.FloatField(default=0)),
                ('avg_takedown_pct', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_odds', models.FloatField()),
                ('blue_odds', models.FloatField()),
                ('predicted_winner', models.CharField(max_length=10)),
                ('prediction_confidence', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blue_fighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blue_fights', to='predictor.fighter')),
                ('red_fighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='red_fights', to='predictor.fighter')),
            ],
        ),
    ]
