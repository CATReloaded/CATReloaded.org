from django.contrib import admin

from .models import Session, Speaker


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    display_list = ('title', 'speaker', 'date_time')
    list_filter = ['speaker', 'date_time']
    search_fields = ('title', )


class SessionInline(admin.StackedInline):
    model = Session
    extra = 1

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'bio')
    inlines = [SessionInline, ]
