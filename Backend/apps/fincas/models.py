import uuid
from django.db import models


class Finca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    hectareas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    propietario_id = models.UUIDField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fincas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
