# Generated by Django 4.0.4 on 2022-05-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
