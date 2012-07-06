# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProposalType'
        db.create_table('proposal_proposaltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('proposal', ['ProposalType'])

        # Adding model 'Category'
        db.create_table('proposal_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('proposal', ['Category'])

        # Adding model 'AudienceLevel'
        db.create_table('proposal_audiencelevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('proposal', ['AudienceLevel'])

        # Adding model 'Proposal'
        db.create_table('proposal_proposal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proposal.ProposalType'])),
            ('audience', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proposal.AudienceLevel'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proposal.Category'])),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('proposal', ['Proposal'])


    def backwards(self, orm):
        # Deleting model 'ProposalType'
        db.delete_table('proposal_proposaltype')

        # Deleting model 'Category'
        db.delete_table('proposal_category')

        # Deleting model 'AudienceLevel'
        db.delete_table('proposal_audiencelevel')

        # Deleting model 'Proposal'
        db.delete_table('proposal_proposal')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proposal.ProposalType']"})
        },
        'proposal.proposaltype': {
            'Meta': {'object_name': 'ProposalType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['proposal']