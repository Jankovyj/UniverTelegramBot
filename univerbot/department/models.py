from django.db import models
from django.utils.translation import ugettext as _


class Department(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'),
                                   blank=True, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    GROUP_TYPES = (('B', _('B')),
                   ('MS', _('MS')),
                   ('M', _('M')))
    
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    department = models.ForeignKey(Department, verbose_name=_('Department'),
                                   related_name='groups')
    year = models.PositiveIntegerField(verbose_name=_('Year'))
    group_type = models.CharField(max_length=2, choices=GROUP_TYPES,
                                  verbose_name=_('Group type'))

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'),
                                   blank=True, null=True)

    def __str__(self):
        return self.name
    
