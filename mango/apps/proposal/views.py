from django.shortcuts import render

from proposal.forms import ProposalForm


def proposal_list(request):
    context = {}
    return render(request, 'proposal/proposal_list.html', context)


def proposal_create(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ProposalForm()
    context = {
        'form': form
    }
    return render(request, 'proposal/proposal_create.html', context)
