.. :changelog:

History
-------

0.1-dev (2012-07-04)
+++++++++++++++++++

- Added basic generic and proposal apps
- Added base.html and home.html templates with twitter bootstrap assets

0.1-dev (2012-07-07)
+++++++++++++++++++

- Added the models ProposalType, Category, AudienceLevel and Proposal
- Added south as depedency
- Added widgets TimeDurationWidget and TimeDurationHiddenWidget
- Added form field TimeDurationField

NOTES:
- Run manage.py syncdb to create south tables
- Run manage.py migrate proposal to execute migrations
