# Generated by Django 4.2.3 on 2023-07-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_organ_id_alter_panel_id_alter_test_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
