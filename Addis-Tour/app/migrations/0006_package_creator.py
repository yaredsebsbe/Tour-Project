# Generated by Django 4.2.6 on 2023-11-13 17:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_package_packagedescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.guide'),
            preserve_default=False,
        ),
    ]