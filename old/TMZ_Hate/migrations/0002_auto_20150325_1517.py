# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMZ_Hate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entities',
            old_name='entity_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='entities',
            old_name='entity_type',
            new_name='type',
        ),
    ]
