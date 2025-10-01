from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    entry_date = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"