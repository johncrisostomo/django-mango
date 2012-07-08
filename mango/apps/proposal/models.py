from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


PROPOSAL_STATUS = (
    ('pending', _(u'Pending')),
    ('approved', _(u'Approved')),
    ('declined', _(u'Declined'))
)


class ProposalType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.name


class AudienceLevel(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Proposal(models.Model):
    user = models.ForeignKey(User, related_name='proposals')
    title = models.CharField(max_length=200)
    type = models.ForeignKey(ProposalType)
    audience = models.ForeignKey(AudienceLevel)
    category = models.ForeignKey(Category)
    is_extreme = models.BooleanField(
        default=False, help_text=_(u"Check if this is an extreme talk"))
    duration = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    abstract = models.TextField()
    status = models.CharField(
        max_length=10, choices=PROPOSAL_STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('proposal_detail', None, {'proposal_id': self.id})
