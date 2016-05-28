from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

from schedule import views

router = routers.DefaultRouter()
router.register(r'timetables', views.SubjectScheduleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
