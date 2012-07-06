from django.contrib import admin

from proposal.models import ProposalType, Category, AudienceLevel, Proposal


admin.site.register(ProposalType)
admin.site.register(Category)
admin.site.register(AudienceLevel)
admin.site.register(Proposal)
