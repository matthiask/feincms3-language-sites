# Generated by Django 2.1.5 on 2019-02-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("feincms3_sites", "0003_site_default_language")]

    operations = [
        migrations.AddField(
            model_name="site",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="is active"),
        )
    ]
