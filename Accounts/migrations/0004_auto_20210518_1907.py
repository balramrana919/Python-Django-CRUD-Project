# Generated by Django 2.1 on 2021-05-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20210518_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='studentss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.students'),
        ),
    ]
