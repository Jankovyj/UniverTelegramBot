from rest_framework import viewsets
from .serializers import SubjectScheduleSerializer
from .models import SubjectSchedule


class SubjectScheduleViewSet(viewsets.ModelViewSet):
    queryset = SubjectSchedule.objects.all()
    serializer_class = SubjectScheduleSerializer
