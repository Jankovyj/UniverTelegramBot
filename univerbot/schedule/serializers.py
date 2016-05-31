from rest_framework import serializers
from .models import SubjectSchedule


class SubjectScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectSchedule
        fields = '__all__'

