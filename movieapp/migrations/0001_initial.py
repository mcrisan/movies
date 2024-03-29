# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'movieapp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tmdb_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'movieapp', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'movieapp_category')


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['movieapp']