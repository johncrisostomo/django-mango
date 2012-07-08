from django import forms
from django.utils.translation import ugettext_lazy as _

from proposal.models import Proposal
from proposal.fields import TimeDurationField


class ProposalForm(forms.ModelForm):
    duration = TimeDurationField(required=False, help_text="Hello World")
    class Meta:
        model = Proposal

    def clean(self):
        data = self.cleaned_data
        if data['is_extreme']:  # if its extreme, duration is not required
            del self._errors['duration']
        return data
