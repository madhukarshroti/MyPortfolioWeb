from django.contrib import admin
from Certificates.models import Certificate

class ProjectAdmin(admin.ModelAdmin):
    list_display=('Certificate_name','image','Certificate_tag','Certificate_date')
# Register your models here.

admin.site.register(Certificate,ProjectAdmin)
