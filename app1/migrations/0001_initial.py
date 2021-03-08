# Generated by Django 3.1.5 on 2021-01-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=50)),
                ('texto', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]