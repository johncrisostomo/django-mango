from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from proposal.models import Proposal


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # Speaker profile
    proposal = models.ForeignKey(Proposal, null=True)
    url = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
