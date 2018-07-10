from django.contrib import admin
from .models import Event

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["name", "organiser", "date"]
	list_display_links = ["name"]
	list_editable = ["name"]
	list_filter = ["updated", "date"]
	search_fields = ["name", "description"]

	class Meta:
		model = Event

admin.site.register(Event)
