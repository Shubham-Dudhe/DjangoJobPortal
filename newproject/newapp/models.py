from django.db import models
import os
from newproject import settings
from django.utils.timezone import now


def files_path():
    return os.path.join(settings.BASE_DIR, 'pythonfile')

class JobPortals(models.Model):
    company_name = models.CharField(max_length=100)
    script_path = models.FilePathField(path=files_path)
    parameter = models.JSONField()
    datetime = models.DateTimeField(default=now)

class ScheduleJob(models.Model):
    schedule_time = models.DateTimeField()
    parameter = models.JSONField()
    job_portals = models.ForeignKey(JobPortals, on_delete=models.CASCADE)
