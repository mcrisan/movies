# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.imdb_id'
        db.add_column(u'movieapp_movie', 'imdb_id',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.overview'
        db.add_column(u'movieapp_movie', 'overview',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.popularity'
        db.add_column(u'movieapp_movie', 'popularity',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.revenue'
        db.add_column(u'movieapp_movie', 'revenue',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.runtime'
        db.add_column(u'movieapp_movie', 'runtime',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.tagline'
        db.add_column(u'movieapp_movie', 'tagline',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Movie.budget'
        db.add_column(u'movieapp_movie', 'budget',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.imdb_id'
        db.delete_column(u'movieapp_movie', 'imdb_id')

        # Deleting field 'Movie.overview'
        db.delete_column(u'movieapp_movie', 'overview')

        # Deleting field 'Movie.popularity'
        db.delete_column(u'movieapp_movie', 'popularity')

        # Deleting field 'Movie.revenue'
        db.delete_column(u'movieapp_movie', 'revenue')

        # Deleting field 'Movie.runtime'
        db.delete_column(u'movieapp_movie', 'runtime')

        # Deleting field 'Movie.tagline'
        db.delete_column(u'movieapp_movie', 'tagline')

        # Deleting field 'Movie.budget'
        db.delete_column(u'movieapp_movie', 'budget')


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.movie': {
            'Meta': {'object_name': 'Movie'},
            'budget': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movieapp.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'overview': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'poster_path': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'revenue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['movieapp']