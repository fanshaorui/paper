# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'customerExample'
        db.delete_table(u'cms_customerexample')

        # Deleting model 'writerExample'
        db.delete_table(u'cms_writerexample')


    def backwards(self, orm):
        # Adding model 'customerExample'
        db.create_table(u'cms_customerexample', (
            ('sci', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('require', self.gf('django.db.models.fields.CharField')(max_length=250)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cms', ['customerExample'])

        # Adding model 'writerExample'
        db.create_table(u'cms_writerexample', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('income', self.gf('django.db.models.fields.CharField')(max_length=250)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cms', ['writerExample'])


    models = {
        u'cms.friendlink': {
            'Meta': {'object_name': 'friendlink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['cms']