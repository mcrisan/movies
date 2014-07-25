# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Keyword'
        db.create_table(u'movieapp_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tmdb_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'movieapp', ['Keyword'])

        # Adding model 'Config'
        db.create_table(u'movieapp_config', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('size1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size6', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size7', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'movieapp', ['Config'])

        # Adding model 'Image'
        db.create_table(u'movieapp_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('vote_average', self.gf('django.db.models.fields.FloatField')()),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')()),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['movieapp.Movie'], null=True, blank=True)),
        ))
        db.send_create_signal(u'movieapp', ['Image'])

        # Adding M2M table for field keywords on 'Movie'
        m2m_table_name = db.shorten_name(u'movieapp_movie_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movieapp.movie'], null=False)),
            ('keyword', models.ForeignKey(orm[u'movieapp.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'keyword_id'])


    def backwards(self, orm):
        # Deleting model 'Keyword'
        db.delete_table(u'movieapp_keyword')

        # Deleting model 'Config'
        db.delete_table(u'movieapp_config')

        # Deleting model 'Image'
        db.delete_table(u'movieapp_image')

        # Removing M2M table for field keywords on 'Movie'
        db.delete_table(db.shorten_name(u'movieapp_movie_keywords'))


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.config': {
            'Meta': {'object_name': 'Config'},
            'base_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size6': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size7': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'movieapp.image': {
            'Meta': {'object_name': 'Image'},
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['movieapp.Movie']", 'null': 'True', 'blank': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'movieapp.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.movie': {
            'Meta': {'object_name': 'Movie'},
            'backdrop_path': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movieapp.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['movieapp.Keyword']", 'null': 'True', 'blank': 'True'}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'overview': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'poster_path': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 25, 0, 0)'}),
            'revenue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'vote_average': ('django.db.models.fields.FloatField', [], {}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {})
        },
        u'movieapp.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['movieapp.Movie']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['movieapp']