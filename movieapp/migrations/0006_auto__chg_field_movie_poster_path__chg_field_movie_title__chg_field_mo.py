# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.poster_path'
        db.alter_column(u'movieapp_movie', 'poster_path', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Movie.title'
        db.alter_column(u'movieapp_movie', 'title', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Movie.original_title'
        db.alter_column(u'movieapp_movie', 'original_title', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):

        # Changing field 'Movie.poster_path'
        db.alter_column(u'movieapp_movie', 'poster_path', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'Movie.title'
        db.alter_column(u'movieapp_movie', 'title', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'Movie.original_title'
        db.alter_column(u'movieapp_movie', 'original_title', self.gf('django.db.models.fields.CharField')(max_length=70))

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
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'poster_path': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['movieapp']