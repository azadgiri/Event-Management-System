from django.contrib import admin
from .models import Event, Registration

admin.site.site_header = "Event Management System"
admin.site.site_title = "Event Management System"
admin.site.index_title = "Admin Panel"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location')
    search_fields = ('title', 'location')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('attendee_name', 'attendee_email', 'event', 'registered_at')
    list_filter = ('event', 'registered_at')
    search_fields = ('attendee_name', 'attendee_email', 'event__title')
