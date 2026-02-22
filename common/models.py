from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

class SchollClass(models.Model):
    start_year = models.IntegerField()
    letter = models.CharField(max_length=1)

class StudentClass(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    school_class = models.ForeignKey('SchollClass', on_delete=models.CASCADE)

class Contacts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_name = models.CharField(max_length=20)
    description = models.TextField()
    home_work = models.TextField()
    shool_class = models.ForeignKey('SchollClass', on_delete=models.CASCADE)

class File(models.Model):
    file_path = models.FileField(upload_to='files/')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

class Grades(models.Model):
    student = models.ForeignKey('Subject', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Student_Home_Work(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    text_data = models.TextField()
    grade = models.ForeignKey('Grades', on_delete=models.CASCADE)

class Losson_Visits(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)