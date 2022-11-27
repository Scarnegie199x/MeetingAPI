from django.contrib import admin
from .models import Meeting, Topic

class TopicInline(admin.TabularInline):
    model = Topic


class MeetingAdmin(admin.ModelAdmin):
    inlines = [
        TopicInline,
    ]


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Topic)



