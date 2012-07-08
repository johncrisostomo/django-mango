from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext as _

from proposal.forms import ProposalForm
from proposal.models import Proposal


def proposal_list(request):
    proposals = Proposal.objects.all().select_related()
    context = {
        'proposals': proposals
    }
    return render(request, 'proposal/proposal_list.html', context)


def proposal_create(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                _(u"Your proposal has been submitted."))
            return redirect('proposal_list')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                _(u"An error occured while trying to submit your proposal."))
    else:
        form = ProposalForm()
    context = {
        'form': form
    }
    return render(request, 'proposal/proposal_create.html', context)


def proposal_detail(request):
    pass
