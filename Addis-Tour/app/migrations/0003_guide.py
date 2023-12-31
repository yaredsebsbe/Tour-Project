# Generated by Django 4.2.6 on 2023-11-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_package_packageimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guideFname', models.CharField(max_length=30)),
                ('guideLname', models.CharField(max_length=30)),
                ('guideQualification', models.CharField(max_length=30)),
                ('guidePhone', models.CharField(max_length=15)),
                ('guidePic', models.ImageField(upload_to='images/')),
                ('guideEmail', models.CharField(max_length=30)),
                ('guidePassword', models.CharField(max_length=15)),
                ('registeredDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
