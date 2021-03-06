# Generated by Django 3.1.4 on 2020-12-17 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField()),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.board')),
            ],
            options={
                'db_table': 'boardlikes',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField()),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.comment')),
            ],
            options={
                'db_table': 'commentlikes',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('nickname', models.CharField(max_length=20)),
                ('privacy_agreement', models.BooleanField(default=False)),
                ('anonymous', models.BooleanField(default=False)),
                ('random_number', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=100)),
                ('board_like', models.ManyToManyField(through='user.BoardLike', to='board.Board')),
                ('comment_like', models.ManyToManyField(through='user.CommentLike', to='board.Comment')),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='RecentView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.member')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
            options={
                'db_table': 'recentviews',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='member_recentview',
            field=models.ManyToManyField(through='user.RecentView', to='product.Product'),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.member'),
        ),
        migrations.AddField(
            model_name='boardlike',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.member'),
        ),
    ]
