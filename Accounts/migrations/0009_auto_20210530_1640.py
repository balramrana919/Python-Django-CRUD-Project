# Generated by Django 2.1 on 2021-05-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_feesprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='advance',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='fees',
            name='amountpaid',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='fees',
            name='duetobepaid',
            field=models.IntegerField(default=True),
        ),
    ]
