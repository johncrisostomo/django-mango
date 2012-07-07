from django.core import validators
from django.forms import CharField, ChoiceField, MultiValueField
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from proposal.widgets import TimeDurationWidget, TimeDurationHiddenWidget


TIME_DURATION_CHOICES = (
    ('hours', _(u'Hours')),
    ('minutes', _(u'Minutes')),
)


class TimeDurationField(MultiValueField):
    widget = TimeDurationWidget(choices=TIME_DURATION_CHOICES)
    hidden_widget = TimeDurationHiddenWidget
    default_error_messages = {
        'required': _(u'Enter a duration value.'),
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (CharField(error_messages={'required': errors['required']}),
                  ChoiceField(choices=TIME_DURATION_CHOICES))
        super(TimeDurationField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in validators.EMPTY_VALUES:
                raise ValidationError(self.error_messages['required'])
            return ' '.join(data_list)
        return None
