# Generated by Django 3.2.4 on 2021-07-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
