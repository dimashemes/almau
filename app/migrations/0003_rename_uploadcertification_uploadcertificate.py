# Generated by Django 5.0.3 on 2024-03-09 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_verification_code_user_verified'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadCertification',
            new_name='UploadCertificate',
        ),
    ]
