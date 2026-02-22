from django.urls import path

from . import views

urlpatterns = [
    path('', views.parents_page, name='parents_page'),
    path('student/<student_id>', views.parent_student, name='parent_student'),
    path('lessons/<lesson_id>/', views.parents_lessons, name='parents_lessons'),
]