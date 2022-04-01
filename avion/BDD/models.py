from django.db import models

# Create your models here.


class AvionModele(models.Model):
    nom = models.CharField(max_length=30,null=True)

class Escadron(models.Model):
    nom =  models.CharField(max_length=30,null=True)
    
class Base(models.Model):
    nom = models.CharField(max_length=30,null=True)
    ville = models.CharField(max_length=30,null=True)
    num = models.IntegerField(max_length=5,null=True)

class Avion(models.Model):
    modele = models.ForeignKey(AvionModele, on_delete=models.CASCADE)
    code_avion = models.CharField(max_length=30)
    escadron = models.ForeignKey(Escadron, on_delete=models.SET_NULL,null=True)
    base = models.ForeignKey(Base, on_delete=models.SET_NULL,null=True)
    date_service = models.DateField()


