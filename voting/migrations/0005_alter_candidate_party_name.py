# Generated by Django 5.0.2 on 2024-02-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_remove_position_party_name_candidate_party_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_name',
            field=models.CharField(max_length=150),
        ),
    ]
