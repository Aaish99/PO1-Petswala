# Generated by Django 3.2.8 on 2022-02-11 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220210_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='RescueServices',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('service_information', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='RescueService',
        ),
    ]