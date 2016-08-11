from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, CourseAdmin)


class PresenceAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('student', 'created_at', 'course')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import StringIO
        f = StringIO.StringIO()
        writer = csv.writer(f)
        writer.writerow(["student", "created_at", "course"])
        for s in queryset:
            writer.writerow([s.student, s.created_at, s.course])
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

    download_csv.short_description = "Download CSV file."

admin.site.register(Presence, PresenceAdmin)


class ClassRoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClassRoom, ClassRoomAdmin)
