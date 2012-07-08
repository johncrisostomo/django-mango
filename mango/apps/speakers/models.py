from django.db import models
import proposal


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    proposal = models.ForeignKey(proposal.models.Proposal)
    url = models.CharField(max_length=255)
    bio = models.TextField()

    def __unicode__(self):
        return self.name
