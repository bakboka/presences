from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^students$', StudentList.as_view(), name='students-list'),
    url(r'^students/(?P<pk>\d+)', StudentDetail.as_view(), name='students-detail'),
    url(r'^courses$', CourseList.as_view(), name='courses-list'),
    url(r'^courses/(?P<pk>\d+)', CourseDetail.as_view(), name='courses-detail'),
    url(r'presences$', PresenceList.as_view(), name='presence-list'),
    url(r'presences/(?P<pk>\d+)', PresenceDetail.as_view(), name='presence-detail'),
    url(r'questions$', QuestionList.as_view(), name='question-list'),
    url(r'questions/(?P<pk>\d+)', QuestionDetail.as_view(), name='question-detail'),
    url(r'classroom$', ClassRoomList.as_view(), name='classroom-list'),
    url(r'classroom/(?P<pk>\d+)', ClassRoomDetail.as_view(), name='classroom-detail'),
    url(r'queue/(?P<id>\d+)', Queue.as_view(), name='queue'),
]