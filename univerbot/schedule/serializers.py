from rest_framework import serializers
from .models import SubjectSchedule


class SubjectScheduleSerializer(serializers.HyperlinkedModelSerializer):
    subject = serializers.ReadOnlyField(source='subject.name')
    teacher = serializers.ReadOnlyField(source='teacher.name')
    time = serializers.ReadOnlyField(source='time.number')
    group = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = SubjectSchedule
        fields = ('subject', 'teacher', 'cabinet', 'time', 'group', 'week_day')

