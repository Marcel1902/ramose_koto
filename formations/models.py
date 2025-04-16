from django.db import models
from students.models import Student

class Modules(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    formateur = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.titre

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    modules = models.ForeignKey(Modules,on_delete=models.CASCADE)
    support_pdf = models.FileField(upload_to='supports/', blank=True, null=True)
    image = models.ImageField(upload_to='formations/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    duree = models.IntegerField(help_text="Durée en heures",null=True, blank=True)

    def __str__(self):
        return self.titre


class FormationRegister(models.Model):
    mmodule_formation = models.ForeignKey(Modules, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_inscription_au_formation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} {self.formation.titre}"