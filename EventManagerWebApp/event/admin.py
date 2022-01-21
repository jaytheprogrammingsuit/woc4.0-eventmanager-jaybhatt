import imp
from django.contrib import admin

from event.models import event_tbl
from event.models import participant_tbl

# Register your models here.
admin.site.register(event_tbl)
admin.site.register(participant_tbl)