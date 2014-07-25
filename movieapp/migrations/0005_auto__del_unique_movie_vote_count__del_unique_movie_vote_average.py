# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Movie', fields ['vote_average']
        db.delete_unique(u'movieapp_movie', ['vote_average'])

        # Removing unique constraint on 'Movie', fields ['vote_count']
        db.delete_unique(u'movieapp_movie', ['vote_count'])


    def backwards(self, orm):
        # Adding unique constraint on 'Movie', fields ['vote_count']
        db.create_unique(u'movieapp_movie', ['vote_count'])

        # Adding unique constraint on 'Movie', fields ['vote_average']
        db.create_unique(u'movieapp_movie', ['vote_average'])


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.movie': {
            'Meta': {'object_name': 'Movie'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movieapp.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'poster_path': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['movieapp']