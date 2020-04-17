# Generated by Django 3.0.4 on 2020-04-10 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Amount', models.FloatField()),
                ('Amount_to_be_Paid', models.FloatField()),
                ('Mode_Of_Transfer', models.CharField(max_length=50)),
                ('Transferred_by', models.CharField(max_length=60)),
                ('Transferred_to', models.CharField(max_length=60)),
                ('Time_of_transfer', models.DateTimeField(auto_now_add=True)),
                ('Transaction_id', models.IntegerField()),
                ('Project_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='credits.Transaction')),
                ('Amount_Remaining', models.FloatField()),
                ('User_id', models.IntegerField()),
                ('totalamount', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='credits.Transaction')),
            ],
            bases=('credits.transaction',),
        ),
    ]
