from django.db import models

# Create your models here.
class empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50,  blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    Salary = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
    telefono = models.CharField(max_length=8,  blank=True, null=False)
    direcciono = models.TextField(blank=False, null=False)

class pc(models.Model):
    pk_pc = models.AutoField(primary_key=True, blank=False, null=False, )
    marca = models.CharField(max_length=80,  null=False, blank=False)
    Ram = models.CharField(max_length=100, null=False, blank=False)
    almacenamiento = models.BigIntegerField(null=False, blank=False)
    modelo = models.CharField(max_length=4, null=False, blank=False)