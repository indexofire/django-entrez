# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'room_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'room', ['Room'])

        # Adding M2M table for field members on 'Room'
        m2m_table_name = db.shorten_name(u'room_room_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'room.room'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['room_id', 'user_id'])

        # Adding model 'RoomEntry'
        db.create_table(u'room_roomentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Room'])),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entrez.EntrezEntry'])),
            ('link_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'room', ['RoomEntry'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'room_room')

        # Removing M2M table for field members on 'Room'
        db.delete_table(db.shorten_name(u'room_room_members'))

        # Deleting model 'RoomEntry'
        db.delete_table(u'room_roomentry')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entrez.entrezentry': {
            'Meta': {'ordering': "['creation_time']", 'object_name': 'EntrezEntry'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastedit_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'magzine': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_owner'", 'to': u"orm['auth.User']"}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_term'", 'to': u"orm['entrez.EntrezTerm']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'entrez.entrezterm': {
            'Meta': {'ordering': "['creation_date']", 'object_name': 'EntrezTerm'},
            'creation_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'db': ('django.db.models.fields.CharField', [], {'default': "'pubmed'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastedit_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'term_owner'", 'to': u"orm['auth.User']"}),
            'period': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '7'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'term': ('django.db.models.fields.TextField', [], {})
        },
        u'room.room': {
            'Meta': {'object_name': 'Room'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': u"orm['auth.User']"}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'member'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'room.roomentry': {
            'Meta': {'object_name': 'RoomEntry'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entrez.EntrezEntry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_time': ('django.db.models.fields.DateTimeField', [], {}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['room.Room']"})
        }
    }

    complete_apps = ['room']