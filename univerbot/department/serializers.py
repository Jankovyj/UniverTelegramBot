from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):

    timetables = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('pk', 'name', 'timetables')

    def get_timetables(self, obj):
        return obj.group_all_schedules_by_days()