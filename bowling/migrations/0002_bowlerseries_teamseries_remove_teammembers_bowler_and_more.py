# Generated by Django 4.2.6 on 2023-11-05 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BowlerSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=1)),
                ('handicap', models.IntegerField(default=0)),
                ('no_handicap', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='bowler',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='team',
        ),
        migrations.AddField(
            model_name='game',
            name='robot_bowled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='league',
            name='players_per_team',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='week',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bowling.league'),
        ),
        migrations.AlterField(
            model_name='league',
            name='league_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Series',
        ),
        migrations.DeleteModel(
            name='TeamMembers',
        ),
        migrations.AddField(
            model_name='teamseries',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bowling.league'),
        ),
        migrations.AddField(
            model_name='teamseries',
            name='left_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='left_team', to='bowling.team'),
        ),
        migrations.AddField(
            model_name='teamseries',
            name='right_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='right_team', to='bowling.team'),
        ),
        migrations.AddField(
            model_name='teamseries',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bowling.week'),
        ),
        migrations.AddField(
            model_name='bowlerseries',
            name='team_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bowling.teamseries'),
        ),
        migrations.AddField(
            model_name='game',
            name='bowler_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bowling.bowlerseries'),
        ),
    ]