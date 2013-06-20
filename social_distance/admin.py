__author__ = 'sgorantla'
from social_distance.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin (admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['question']}),
        ('Data Informantion', {'fields' : ['pub_date'], 'classes' : ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
