# Generated by Django 2.2.1 on 2020-07-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggUsageRecordsDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_date', models.DateField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('resource_used', models.IntegerField()),
                ('usage_type', models.CharField(choices=[('data', 'Data'), ('voice', 'Voice')], default='data', max_length=10)),
                ('usage_records', models.ManyToManyField(to='usage.UsageRecord')),
            ],
        ),
    ]
