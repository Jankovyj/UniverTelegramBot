from django.db import models
from django.utils.translation import ugettext as _

from department.models import Department, Group

class Student(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    surname = models.CharField(verbose_name=_('Surname'), max_length=50)
    mobile = models.CharField(verbose_name=_('Mobile'), max_length=50)
    group = models.ForeignKey(Group, verbose_name=_('Group'),
                              related_name='students')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)

class Teacher(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    surname = models.CharField(verbose_name=_('Surname'), max_length=50)
    mobile = models.CharField(verbose_name=_('Mobile'), max_length=50)
    department = models.ForeignKey(Department, verbose_name=_('Department'),
                                   related_name='teachers')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)
