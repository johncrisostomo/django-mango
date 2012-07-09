from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render


def list(request):
    speakers = User.objects.filter(
        groups__name__exact=settings.SPEAKERS_GROUP_NAME)
    context = {
        'speakers': speakers
    }
    return render(request, 'speakers/list.html', context)
