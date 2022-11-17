from django.contrib import admin
from .models import List_Jobs, Python, Command, Sysadmin, Latest


class Host(admin.ModelAdmin):
	list_display = ['title', 'link']
admin.site.register(List_Jobs, Host)
admin.site.register(Python, Host)
admin.site.register(Command, Host)
admin.site.register(Sysadmin, Host)
admin.site.register(Latest, Host)