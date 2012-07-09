from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import generic


class UserProfileInline(admin.TabularInline):
    model = generic.models.UserProfile
    fk_name = 'user'
    can_delete = False
    max_num = 1
    verbose_name_plural = 'User Profile'


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
