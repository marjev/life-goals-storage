# Generated by Django 4.2.1 on 2023-05-28 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CseEndeavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerScienceEducatorsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack_exchange_id', models.IntegerField(unique=True)),
                ('type', models.CharField(choices=[('QS', 'Question'), ('AN', 'Answer'), ('CM', 'Comment')], default='QS', max_length=2)),
                ('text', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='red.cseendeavour')),
            ],
        ),
    ]
