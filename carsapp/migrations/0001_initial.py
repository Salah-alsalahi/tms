# Generated by Django 4.0.6 on 2022-08-02 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(blank=True, help_text='اسم صاحب السيارة ', max_length=60)),
                ('C_number', models.IntegerField(unique=True)),
                ('privGovTaxi', models.CharField(choices=[('Private', 'Private'), ('Goverment', 'Goverment'), ('Taxi', 'Taxi')], default='Private', help_text='اجرة - خصوصي - عمومي', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VIOLATION',
            fields=[
                ('V_number', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('cost', models.PositiveIntegerField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('IsPaid', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violations', to='carsapp.car')),
            ],
        ),
        migrations.CreateModel(
            name='CUSTOMER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_number', models.IntegerField(blank=True, default=None, null=True, unique=True)),
                ('account', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car', to='carsapp.car')),
            ],
        ),
    ]
