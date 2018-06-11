from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved', 'start_date', 'created_at',)


# Register your models here.
admin.site.register(Event, EventAdmin)
