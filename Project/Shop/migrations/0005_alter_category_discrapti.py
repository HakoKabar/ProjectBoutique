# Generated by Django 3.2.8 on 2021-10-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_rename_date_update_category_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='discrapti',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]