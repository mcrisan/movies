# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field categories on 'Movies'
        m2m_table_name = db.shorten_name(u'movieapp_movies_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movies', models.ForeignKey(orm[u'movieapp.movies'], null=False)),
            ('category', models.ForeignKey(orm[u'movieapp.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movies_id', 'category_id'])


    def backwards(self, orm):
        # Removing M2M table for field categories on 'Movies'
        db.delete_table(db.shorten_name(u'movieapp_movies_categories'))


    models = {
        u'movieapp.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'tmdb_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'movieapp.movies': {
            'Meta': {'object_name': 'Movies'},
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