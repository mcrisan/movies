# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movies'
        db.create_table(u'movieapp_movies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tmdb_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('original_title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('poster_path', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('vote_average', self.gf('django.db.models.fields.FloatField')(unique=True)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'movieapp', ['Movies'])


    def backwards(self, orm):
        # Deleting model 'Movies'
        db.delete_table(u'movieapp_movies')


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.movies': {
            'Meta': {'object_name': 'Movies'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'poster_path': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {'unique': 'True'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['movieapp']