from django.db import models

# Create your models here.


class Project(models.Model):
    project_title = models.CharField(max_length=100)
    pillar = models.CharField(max_length=100)
    name_of_beneficiaries = models.CharField(max_length=100)
    number_of_beneficiaries = models.IntegerField()
    number_of_male = models.IntegerField()
    number_of_female = models.IntegerField()
    region = models.CharField(max_length=100)
    implementing_partner = models.CharField(max_length=150)

    def __str__(self):
        return self.project_title
