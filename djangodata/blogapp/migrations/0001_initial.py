# Generated by Django 3.0.7 on 2020-07-28 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogClass',
            fields=[
                ('classid', models.Field(primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=45)),
                ('classstate', models.IntegerField()),
            ],
        ),
    ]
