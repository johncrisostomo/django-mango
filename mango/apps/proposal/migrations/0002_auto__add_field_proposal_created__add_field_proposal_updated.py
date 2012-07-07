# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proposal.created'
        db.add_column('proposal_proposal', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime.now(), blank=True),
                      keep_default=False)

        # Adding field 'Proposal.updated'
        db.add_column('proposal_proposal', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Proposal.created'
        db.delete_column('proposal_proposal', 'created')

        # Deleting field 'Proposal.updated'
        db.delete_column('proposal_proposal', 'updated')


    models = {
        'proposal.audiencelevel': {
            'Meta': {'object_name': 'AudienceLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'proposal.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'proposal.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'audience': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proposal.AudienceLevel']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proposal.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proposal.ProposalType']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'proposal.proposaltype': {
            'Meta': {'object_name': 'ProposalType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['proposal']