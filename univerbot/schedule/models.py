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
    WEEK_DAYS = (('1', _('Monday')), ('2', _('Tuesday')),
                 ('3', _('Wednesday')), ('4', _('Thursday')),
                 ('5', _('Friday')), ('6', _('Saturday')),
                 ('7', _('Sunday')))

    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    teacher = models.ForeignKey(Teacher, verbose_name=_('Teacher'))
    cabinet = models.PositiveIntegerField(verbose_name=_('Cabinet'))
    time = models.ForeignKey(RingsSchedule, verbose_name=_('Time'))
    group = models.ForeignKey(Group, verbose_name=_('Group'),
                              related_name='timetables')
    week_day = models.CharField(max_length=1, choices=WEEK_DAYS,
                                verbose_name=_('Week day'))

    def __str__(self):
        return '%s %s %d' % (self.subject, self.time, self.cabinet)