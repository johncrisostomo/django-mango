from django.contrib import admin

import proposal


# Proposal
admin.site.register(proposal.models.ProposalType)
admin.site.register(proposal.models.Category)
admin.site.register(proposal.models.AudienceLevel)
admin.site.register(proposal.models.Proposal)
