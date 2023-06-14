from django.contrib import admin
from skills.models import Skills

class SkillAdmin(admin.ModelAdmin):
    list_display=("skill_name","skill_value")

admin.site.register(Skills,SkillAdmin)

# Register your models here.
