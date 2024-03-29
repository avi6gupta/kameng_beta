# Generated by Django 2.1 on 2018-08-14 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0003_auto_20180811_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaintText', models.CharField(max_length=500)),
                ('type_of_complaint', models.CharField(max_length=20)),
                ('is_resolved_ct', models.BooleanField(default=False)),
                ('is_resolved_stud', models.BooleanField(default=False)),
                ('reply', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Kamengite')),
            ],
        ),
    ]
