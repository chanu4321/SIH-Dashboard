# Generated by Django 4.2.5 on 2023-10-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('Bulb_Issue', models.CharField(max_length=10)),
                ('Curr_Leak', models.CharField(max_length=10)),
                ('Brok_Wire', models.CharField(max_length=10)),
                ('No_Sgnl', models.CharField(max_length=10)),
            ],
        ),
    ]
