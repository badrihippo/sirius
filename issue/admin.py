from issue.models import Issue, Editorial, Squiggle, UpcomingSquiggle
from django.contrib import admin
admin.site.register(Editorial)
class EditorialInline(admin.StackedInline):
    model = Editorial
    extra = 0
class IssueAdmin(admin.ModelAdmin):
    inlines = [EditorialInline]
admin.site.register(Issue, IssueAdmin)

admin.site.register(Squiggle)
admin.site.register(UpcomingSquiggle)
