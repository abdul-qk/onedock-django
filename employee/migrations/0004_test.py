# Generated by Django 3.1.5 on 2021-02-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_category_cat_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Test',
            },
        ),
    ]
