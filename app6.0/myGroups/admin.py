from django.contrib import admin
from .models import Groups
from .models import Students


class GroupsAdmin(admin.ModelAdmin):
    list_display = ("name",)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "second_last_name")


admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)