# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'friendlink'
        db.create_table(u'cms_friendlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'cms', ['friendlink'])


    def backwards(self, orm):
        # Deleting model 'friendlink'
        db.delete_table(u'cms_friendlink')


    models = {
        u'cms.friendlink': {
            'Meta': {'object_name': 'friendlink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['cms']