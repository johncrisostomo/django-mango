from django import forms

from proposal.models import Proposal


class ProposalEdit(forms.ModelForm):
    class Meta:
        model = Proposal
