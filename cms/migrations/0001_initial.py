# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'writerExample'
        db.create_table(u'cms_writerexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('income', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cms', ['writerExample'])

        # Adding model 'customerExample'
        db.create_table(u'cms_customerexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('sci', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('require', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cms', ['customerExample'])


    def backwards(self, orm):
        # Deleting model 'writerExample'
        db.delete_table(u'cms_writerexample')

        # Deleting model 'customerExample'
        db.delete_table(u'cms_customerexample')


    models = {
        u'cms.customerexample': {
            'Meta': {'object_name': 'customerExample'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'require': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sci': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'cms.writerexample': {
            'Meta': {'object_name': 'writerExample'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['cms']