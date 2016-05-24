from django.db import models
from django.utils.translation import ugettext as _

from account.models import Teacher
from department.models import Group, Subject

class RingsSchedule(models.Model):
    start = models.TimeField(verbose_name=_('Start'))
    end = models.TimeField(verbose_name=_('End'))
    number = models.PositiveIntegerField(verbose_name=_('Number'))

    def __str__(self):
        return '№%d %s - %s' % (self.number, self.start, self.end)


class SubjectSchedule(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    teacher = models.ForeignKey(Teacher, verbose_name=_('Teacher'))
    cabinet = models.PositiveIntegerField(verbose_name=_('Cabinet'))
    time = models.ForeignKey(RingsSchedule, verbose_name=_('Time'))

    def __str__(self):
        return '%s %s %d' % (self.subject, self.time, self.cabinet)


class TimeTable(models.Model):
    WEEK_DAYS = (('1', _('Monday')), ('2', _('Tuesday')),
                 ('3', _('Wednesday')), ('4', _('Thursday')),
                 ('5', _('Friday')), ('6', _('Saturday')),
                 ('7', _('Sunday')))

    group = models.ForeignKey(Group, verbose_name=_('Group'),
                              related_name='timetables')
    week_day = models.CharField(max_length=1, choices=WEEK_DAYS,
                                verbose_name=_('Week day'))
    subjects_schedule = models.ManyToManyField(SubjectSchedule,
                                               verbose_name=_('subjects schedule'))

    
    def __str__(self):
        return '%s %s' % (self.group, self.get_week_day_display())
