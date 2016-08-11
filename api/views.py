from api.serializers import StudentSerializer, CourseSerializer, PresenceSerializer, QuestionSerializer, \
    ClassRoomSerializer
from django.core.serializers import serialize
from django.http.response import JsonResponse, HttpResponse
from presence.models import Student, Presence, Course, Question, ClassRoom
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().exclude(id=1)
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    model = Course
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    model = Course
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PresenceList(generics.ListCreateAPIView):
    queryset = Presence.objects.all()
    model = Presence
    serializer_class = PresenceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PresenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Presence.objects.all()
    model = Presence
    serializer_class = PresenceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    model = Question
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    model = Question
    serializer_class = QuestionSerializer


class ClassRoomList(generics.ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    model = ClassRoom
    serializer_class = ClassRoomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ClassRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    model = ClassRoom
    serializer_class = ClassRoomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Queue(APIView):
    def get(self, request, id):
        queue = Question.objects.all().filter(local_id=id)
        return JsonResponse(serialize('python', queue), safe=False)  # TODO return a Response from django rest api

    def delete(self, request, id):
        Question.objects.all().filter(local_id=id).delete()
        return HttpResponse("all good")
