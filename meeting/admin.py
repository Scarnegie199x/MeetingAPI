from django.contrib import admin
from .models import Meeting, Topic

class TopicInline(admin.TabularInline):
    readonly_fields = ('created_at', 'updated_at')
    model = Topic


class MeetingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    inlines = [
        TopicInline,
    ]


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Topic)



