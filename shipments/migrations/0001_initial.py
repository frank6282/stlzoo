# Generated by Django 5.0.7 on 2024-08-09 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('species', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_label', models.CharField(max_length=20)),
                ('received', models.PositiveSmallIntegerField(default=0)),
                ('bad', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('non', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('doa', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('para', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('released', models.PositiveSmallIntegerField(blank=True, default=0, editable=False, null=True)),
                ('entered', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='species', to='species.species')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier', to='suppliers.suppliers')),
            ],
            options={
                'ordering': ['-shipping_label'],
            },
        ),
    ]