from django.contrib import admin
from schedule.models import (RingsSchedule, SubjectSchedule,
                             TimeTable)

admin.site.register(RingsSchedule)
admin.site.register(SubjectSchedule)
admin.site.register(TimeTable)

