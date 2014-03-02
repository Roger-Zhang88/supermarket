from django.contrib import admin
from models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter=['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
