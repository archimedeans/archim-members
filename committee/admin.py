from django.contrib import admin

from .models import Committee, CommitteeMember

admin.site.register(Committee)
admin.site.register(CommitteeMember)