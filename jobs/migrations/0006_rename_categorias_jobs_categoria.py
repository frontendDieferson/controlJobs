# Generated by Django 4.0.3 on 2022-04-11 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_jobs_categoria_jobs_categorias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='categorias',
            new_name='categoria',
        ),
    ]
