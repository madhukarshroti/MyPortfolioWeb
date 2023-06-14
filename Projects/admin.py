from django.contrib import admin
from Projects.models import ProjectShow

class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','tag','technology','desc')
# Register your models here.

admin.site.register(ProjectShow,ProjectAdmin)
