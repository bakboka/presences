from django.db import models
from datetime import date


class Student(models.Model):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    cursus = models.CharField(max_length=30)

    class Meta:
        unique_together = ('first_name', 'last_name', 'cursus')

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


class Course(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Presence(models.Model):
    student = models.ForeignKey('Student')
    created_at = models.DateField(default=date.today)
    course = models.ForeignKey('Course')

    def __unicode__(self):
        return self.student.get_full_name()


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    student = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey('ClassRoom')
