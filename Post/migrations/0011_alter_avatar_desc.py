# Generated by Django 4.0 on 2022-02-09 03:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_alter_comment_text_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
