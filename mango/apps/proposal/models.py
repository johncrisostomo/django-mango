from django.db import models
from django.utils.translation import ugettext_lazy as _


PROPOSAL_TYPE = (
    (1, _('Talk')),
)

AUDIENCE_LEVEL = (
    (1, _('Novice'))
)


class Proposal(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=30, choices=PROPOSAL_TYPE)
    audience = models.CharField(max_length=30, choices=AUDIENCE_LEVEL)
    category = models.ForeignKey()
    duration = models.
    description = models.TextField()
    abstract = models.TextField()
