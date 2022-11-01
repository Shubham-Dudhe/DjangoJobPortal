from django.contrib import admin
from .models import JobPortals,ScheduleJob
# Register your models here.
class JobPortalsAdmin(admin.ModelAdmin):
    list_display=['id','company_name','parameter','script_path','datetime']

admin.site.register(JobPortals,JobPortalsAdmin)

class ScheduleJobAdmin(admin.ModelAdmin):
    list_display=['id','schedule_time','parameter','job_portals']

admin.site.register(ScheduleJob,ScheduleJobAdmin)