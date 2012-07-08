from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # FIXME: The unicode repr of the instance of this model
    # is being displayed as the label for the type attribute
    type = models.ForeignKey(UserType, null=True)

    # Speaker profile
    url = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
