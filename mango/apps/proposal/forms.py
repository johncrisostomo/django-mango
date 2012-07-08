from django import forms

from proposal.models import Proposal
from proposal.fields import TimeDurationField


class ProposalForm(forms.ModelForm):
    duration = TimeDurationField(required=False)

    class Meta:
        model = Proposal
        exclude = ('status',)

    def clean(self):
        data = self.cleaned_data
        if data['is_extreme']:  # if its extreme, duration is not required
            del self._errors['duration']
        return data
