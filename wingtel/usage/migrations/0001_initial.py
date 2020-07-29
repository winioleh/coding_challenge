# Generated by Django 2.2.1 on 2020-07-29 15:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('usage_date', models.DateField(default=datetime.date(2020, 7, 29))),
                ('usage_type', models.CharField(choices=[('data', 'Data'), ('voice', 'Voice')], default='data', max_length=10)),
                ('resource_used', models.IntegerField(null=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions.Subscription')),
            ],
        ),
    ]