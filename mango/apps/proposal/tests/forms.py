from django.test import TestCase
from django.contrib.auth.models import User

from proposal.models import Proposal, ProposalType, AudienceLevel, Category
from proposal.forms import ProposalForm


class ProposalFormTest(TestCase):
    fixtures = ['proposal_types.json',
                'categories.json',
                'audience_levels.json']

    def setUp(self):
        self.user = User.objects.create_user('marconi',
                                             'marconi@djangomango.com',
                                             'supersecure')

    def test_is_extreme(self):
        """
        Test that if is_extreme is ticked, duration is not required.
        """
        proposal_type = ProposalType.objects.get(name='Talk')
        audience_level = AudienceLevel.objects.get(name='Experienced')
        category = Category.objects.get(name='Web Framework')

        self.assertEqual(Proposal.objects.count(), 0)
        data = {'title': 'Awesome Talk',
                'type': proposal_type.id,
                'audience': audience_level.id,
                'category': category.id,
                'is_extreme': True,
                'duration_0': '',
                'duration_1': 'minutes',
                'description': 'Some awesome description.',
                'abstract': 'Some awesome abstract.'}
        form = ProposalForm(data=data)
        print form.errors
        self.failUnless(form.is_valid())
        form.save(self.user)
        self.assertEqual(Proposal.objects.count(), 1)

    def test_not_is_extreme(self):
        """
        Test that if is_extreme is not ticked, duration is required.
        """
        proposal_type = ProposalType.objects.get(name='Talk')
        audience_level = AudienceLevel.objects.get(name='Experienced')
        category = Category.objects.get(name='Web Framework')

        self.assertEqual(Proposal.objects.count(), 0)
        data = {'title': 'Awesome Talk',
                'type': proposal_type.id,
                'audience': audience_level.id,
                'category': category.id,
                'is_extreme': False,
                'duration_0': '',
                'duration_1': 'minutes',
                'description': 'Some awesome description.',
                'abstract': 'Some awesome abstract.'}
        form = ProposalForm(data=data)
        self.assertFalse(form.is_valid())
