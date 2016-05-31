from rest_framework import serializers
from .models import Group

from schedule.serializers import SubjectScheduleSerializer


class GroupSerializer(serializers.ModelSerializer):

    timetables = SubjectScheduleSerializer(many=True)

    class Meta:
        model = Group
        fields = ('pk', 'name', 'timetables')

