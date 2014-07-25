# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Movies'
        db.delete_table(u'movieapp_movies')

        # Removing M2M table for field categories on 'Movies'
        db.delete_table(db.shorten_name(u'movieapp_movies_categories'))

        # Adding model 'Movie'
        db.create_table(u'movieapp_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tmdb_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('original_title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('poster_path', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('vote_average', self.gf('django.db.models.fields.FloatField')(unique=True)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'movieapp', ['Movie'])

        # Adding M2M table for field categories on 'Movie'
        m2m_table_name = db.shorten_name(u'movieapp_movie_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movieapp.movie'], null=False)),
            ('category', models.ForeignKey(orm[u'movieapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'category_id'])


    def backwards(self, orm):
        # Adding model 'Movies'
        db.create_table(u'movieapp_movies', (
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('poster_path', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('tmdb_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('vote_average', self.gf('django.db.models.fields.FloatField')(unique=True)),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('original_title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'movieapp', ['Movies'])

        # Adding M2M table for field categories on 'Movies'
        m2m_table_name = db.shorten_name(u'movieapp_movies_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movies', models.ForeignKey(orm[u'movieapp.movies'], null=False)),
            ('category', models.ForeignKey(orm[u'movieapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movies_id', 'category_id'])

        # Deleting model 'Movie'
        db.delete_table(u'movieapp_movie')

        # Removing M2M table for field categories on 'Movie'
        db.delete_table(db.shorten_name(u'movieapp_movie_categories'))


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
            'vote_average': ('django.db.models.fields.FloatField', [], {'unique': 'True'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['movieapp']