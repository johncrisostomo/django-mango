from django.shortcuts import render


def proposal_list(request):
    context = {}
    return render(request, 'proposal/proposal_list.html', context)


def proposal_create(request):
    context = {}
    return render(request, 'proposal/proposal_create.html', context)
