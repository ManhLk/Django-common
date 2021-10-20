from django.contrib import admin
from django.db import models
from django import forms
from django.db.models import fields
from django.utils.safestring import mark_safe
from courses.models import Category, Course, Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ["subject", "created_date", "active", "category"]
    list_filter = ["active", "category__name"]
    search_fields = ["subject", "category__name"]
    # Display image
    readonly_fields = ["image_course"]
    def image_course(self, course):
        if course:
            return mark_safe(f'<image src="/static/image/{course.image.name}"" atl="photo" style="width:180px; height:128px;"/>')
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget)
    
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ["subject", "created_date", "updated_date", "active", "course"]
    list_filter = ["active", "subject"]
    search_fields = ["subject", "course__name"]

    # Dispaly image
    readonly_fields = ["lesson_image"]
    def lesson_image(self, lesson):
        if lesson:
            return mark_safe(f'<image src="/static/image/{lesson.image.name}" alt="{lesson.subject}" style="width:180px; height:128px;">')

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
