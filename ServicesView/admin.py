from django.contrib import admin
from ServicesView.models import ServicesSec

class ProjectAdmin(admin.ModelAdmin):
    list_display=('Service','icon','ServiceDetail')
# Register your models here.

admin.site.register(ServicesSec,ProjectAdmin)
