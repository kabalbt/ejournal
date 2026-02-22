from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher_page, name='teacher_page'),
    path('lessons', views.teacher_lessons, name='teacher_lessons'),
    path('lessons/<lessons_id>', views.specific_lesson, name='specific_lesson'),
    path('lessons/<lessons_id>/<absence>', views.absence, name='absence'),
    path('lessons/<lessons_id>/<grade>', views.grade, name='grade'),
    path('lessons/<lessons_id>/homework/<homework_id>', views.student_homework, name='student_homework'),
]