from django.shortcuts import render

# Create your views here.
def parents_page(request):
    return 'ok'

def parent_student(request, student_id):
    return f'ok {student_id}'

def parents_lessons(request, lesson_id):
    return f'ok {lesson_id}'