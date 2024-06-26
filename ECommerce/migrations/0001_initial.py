# Generated by Django 4.2.11 on 2024-06-03 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid
import zango.apps.dynamic_models.fields
import zango.core.storage_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appauth', '0006_appusermodel_app_objects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', zango.core.storage_utils.ZFileField(blank=True, null=True, upload_to=zango.core.storage_utils.RandomUniqueFileName, validators=[zango.core.storage_utils.validate_file_extension])),
                ('price', models.IntegerField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('product', zango.apps.dynamic_models.fields.ZForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
