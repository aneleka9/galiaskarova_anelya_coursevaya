from django.contrib import admin
from .models import User, Course, CourseEnrollment, Module, Comment, Lesson

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(CourseEnrollment)
admin.site.register(Module)
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order')
    fields = ('module', 'title', 'content', 'image', 'video', 'order')


