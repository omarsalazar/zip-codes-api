# Generated by Django 4.2.1 on 2023-10-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zip_codes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettlementTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='SettlementModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField()),
                ('name', models.CharField()),
                ('zone_type', models.CharField()),
                ('settlement_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='settlements.settlementtypemodel')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='zip_codes.zipcodemodel')),
            ],
        ),
    ]
