.. :changelog:

History
-------

0.1-dev (2012-07-09)
+++++++++++++++++++

- Added speakers list view

NOTES:

- For speakers list view to work, add a speakers group and update the `SPEAKERS_GROUP_NAME` setting

0.1-dev (2012-07-08)
+++++++++++++++++++

- Added basic form styles
- Added klass and widget templatetags
- Tweaked field.html so it knows where to place the label when field is a checkbox
- Added django-endless-pagination app as a dependency
- Updated proposal listing
- Added status field to proposal model
- Added tests for ProposalForm
- Added user field to proposal model
- Added save method to ProposalForm which accepts user
- Added bit of js to toggle duration form field if is_extreme is ticked
- Added basic proposal detail page
- Added slug field in proposal model
- Updated proposal_detail url to accept slug instead of id
- Added proposal_update_status view for update proposal status

NOTES:

- Run setup.py develop to install extra dependencies
- Run manage.py migrate proposal to execute migrations

0.1-dev (2012-07-07)
+++++++++++++++++++

- Added the models ProposalType, Category, AudienceLevel and Proposal
- Added south as depedency
- Added widgets TimeDurationWidget and TimeDurationHiddenWidget
- Added form field TimeDurationField
- Added proposal_list and proposal_create views
- Added ProposalForm form
- Added is_extreme field for proposal model
- Added field.html template for individual field rendering

NOTES:

- Run manage.py syncdb to create south tables
- Run manage.py migrate proposal to execute migrations

0.1-dev (2012-07-06)
+++++++++++++++++++

- Added Social Auth

NOTES:

- Run manage.py syncdb to create social auth tables
- Add social auth api tokens to localsettings

0.1-dev (2012-07-04)
+++++++++++++++++++

- Added basic generic and proposal apps
- Added base.html and home.html templates with twitter bootstrap assets
