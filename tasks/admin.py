from django.contrib import admin
from .models import task


class taskAdmin(admin.ModelAdmin):
    list_display = ['task','iscompleted','craeted_at','changed_at']
    search_fields = ['task']
    list_filter = ['iscompleted']

admin.site.register(task,taskAdmin)