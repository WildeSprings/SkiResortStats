# Generated by Django 4.1.4 on 2022-12-13 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activerecord',
            old_name='snow_bae_depth',
            new_name='snow_base_depth',
        ),
    ]
