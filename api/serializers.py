# coding=utf-8
from django.core.exceptions import ValidationError
from rest_framework import serializers
from presence.models import Student, Presence, Course, Question, ClassRoom
import datetime


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student


class PresenceSerializer(serializers.ModelSerializer):
    def validate(self, data):
        student = data["student"]
        course = data["course"]
        today= datetime.date.today()
        present = Presence.objects.all().filter(student=student).filter(created_at=today).filter(course=course)
        if len(present):
            raise ValidationError("L'étudiant s'est déjà inscrit en guidance aujourd'hui", code='invalid')
        return data

    class Meta:
        model = Presence


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course


class QuestionSerializer(serializers.ModelSerializer):
    def validate(self, data):
        present = Question.objects.all().filter(student=data["student"])
        if len(present):
            raise ValidationError("L'étudiant s'est déjà inscrit en guidance aujourd'hui", code='invalid')
        return data

    class Meta:
        model = Question


class ClassRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
