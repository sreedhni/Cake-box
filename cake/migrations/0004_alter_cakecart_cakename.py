# Generated by Django 4.2.5 on 2023-11-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_alter_cakecategory_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakecart',
            name='cakename',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cake.cakevarient'),
        ),
    ]