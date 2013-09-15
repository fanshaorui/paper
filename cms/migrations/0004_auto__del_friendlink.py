# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'friendlink'
        db.delete_table(u'cms_friendlink')


    def backwards(self, orm):
        # Adding model 'friendlink'
        db.create_table(u'cms_friendlink', (
            ('link', self.gf('django.db.models.fields.CharField')(max_length=300)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'cms', ['friendlink'])


    models = {
        
    }

    complete_apps = ['cms']