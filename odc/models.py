from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    socio_professional_category = models.CharField(max_length=50)
    current_address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    level_of_education = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField()
    trainer = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Startup(models.Model):
    student_name = models.CharField(max_length=150)
    project_title = models.CharField(max_length=200)
    project_category = models.CharField(max_length=100)

    def __str__(self):
        return self.project_title
