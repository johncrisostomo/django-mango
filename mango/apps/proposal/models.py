from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    title = models.CharField(max_length=200)
    type = models.ForeignKey(ProposalType)
    audience = models.ForeignKey(AudienceLevel)
    category = models.ForeignKey(Category)
    is_extreme = models.BooleanField(default=False, help_text=_(u"Check if this is an extreme talk"))
    duration = models.CharField(max_length=20)
    description = models.TextField()
    abstract = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title
