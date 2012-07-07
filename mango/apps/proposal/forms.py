from django import forms

from proposal.models import Proposal
from proposal.fields import TimeDurationField


class ProposalForm(forms.ModelForm):
    duration = TimeDurationField()
    class Meta:
        model = Proposal
